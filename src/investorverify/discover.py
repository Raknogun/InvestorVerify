"""Reproducible public-source candidate intake. Discovery != investor verification.

Use the curated source sightings CSV to merge candidate names without altering
previous screening labels. Optional live CzechStartups HTML harvesting exports
headings to a *staging CSV* and never silently treats them as direct VC investors.

Run: python -m investorverify.discover --check
     python -m investorverify.discover --write
     python -m investorverify.discover --fetch-czechstartups
"""
from __future__ import annotations

import argparse
import csv
from datetime import date
from html.parser import HTMLParser
import io
import json
from pathlib import Path
import re
import unicodedata
from urllib.request import Request, urlopen

from .validate import is_public_url

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
CANDIDATE_FIELDS = ["investor_id", "name", "aliases", "country_focus",
                    "category_proposed", "discovery_source_url", "status"]
SIGHTING_FIELDS = ["candidate_name", "category_hint", "source_title",
                   "source_url", "source_year", "accessed_date", "notes"]
DIRECTORY_URL = "https://czechstartups.gov.cz/en/startup-ecosystem/investors/"

def name_key(value: str) -> str:
    """Normalize case, accents, punctuation and spaces; never fuzzy-merge brands."""
    ascii_text = unicodedata.normalize("NFKD", value).casefold()
    ascii_text = "".join(c for c in ascii_text if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "", ascii_text)

def load_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))

def rendered_csv(fields: list[str], rows: list[dict[str, str]]) -> str:
    out = io.StringIO(newline="")
    writer = csv.DictWriter(out, fieldnames=fields, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return out.getvalue()

def index_names(candidates: list[dict[str, str]]) -> dict[str, str]:
    lookup: dict[str, str] = {}
    for row in candidates:
        for name in [row["name"], *row.get("aliases", "").split(";")]:
            normalized = name_key(name)
            if normalized:
                owner = lookup.setdefault(normalized, row["investor_id"])
                if owner != row["investor_id"]:
                    raise ValueError(f"Conflicting exact alias {name!r}: {owner} / {row['investor_id']}")
    return lookup

def merge(candidates: list[dict[str, str]], sightings: list[dict[str, str]]):
    """Return candidates, new rows, and matched duplicate sightings; no deletions."""
    records = [dict(row) for row in candidates]
    lookup = index_names(records)
    used = {r["investor_id"] for r in records}
    next_id = 1
    new_rows, duplicate_matches = [], []
    for item in sightings:
        name = item["candidate_name"].strip()
        key = name_key(name)
        if not key or not is_public_url(item["source_url"]):
            raise ValueError(f"Invalid source/name: {item}")
        if key in lookup:
            duplicate_matches.append((name, lookup[key]))
            continue
        while f"cznew{next_id:03d}" in used:
            next_id += 1
        ident = f"cznew{next_id:03d}"
        used.add(ident)
        record = {
            "investor_id": ident, "name": name, "aliases": "",
            "country_focus": "CZ", "category_proposed": "unknown",
            "discovery_source_url": item["source_url"],
            "status": "discovered_unreviewed"
        }
        records.append(record)
        new_rows.append(record)
        lookup[key] = ident
    return records, new_rows, duplicate_matches

class HeadingCollector(HTMLParser):
    """Collect potential organization names from public HTML H4 headings."""
    def __init__(self):
        super().__init__()
        self.depth = 0
        self.parts: list[str] = []
        self.headings: list[str] = []
    def handle_starttag(self, tag, attrs):
        if tag.lower() == "h4":
            if self.depth == 0:
                self.parts = []
            self.depth += 1
    def handle_data(self, text):
        if self.depth:
            self.parts.append(text)
    def handle_endtag(self, tag):
        if tag.lower() == "h4" and self.depth:
            self.depth -= 1
            if not self.depth:
                heading = " ".join(" ".join(self.parts).split())
                if heading and len(heading) <= 120:
                    self.headings.append(heading)

def parse_directory_headings(html: str) -> list[str]:
    collector = HeadingCollector()
    collector.feed(html)
    return list(dict.fromkeys(collector.headings))

def fetch_directory_staging(data_dir: Path = DATA) -> dict:
    """Optional single-page retrieval; no automatic entry in main candidates file."""
    if not is_public_url(DIRECTORY_URL):
        raise ValueError("Directory URL must be public HTTPS")
    req = Request(DIRECTORY_URL, headers={"User-Agent": "InvestorVerifyResearch/0.1 (public academic take-home)"})
    with urlopen(req, timeout=20) as response:
        html = response.read(3_000_000).decode("utf-8", errors="replace")
    names = parse_directory_headings(html)
    if not names:
        raise ValueError("No H4 organization headings found; inspect changed site layout")
    now = date.today().isoformat()
    rows = [
        {"candidate_name": name, "category_hint": "unclassified_web_heading",
         "source_title": "CzechStartups - Investors directory (live fetch)",
         "source_url": DIRECTORY_URL, "source_year": "",
         "accessed_date": now,
         "notes": "Raw HTML heading only. Must be reviewed before merging; may include associations and intermediaries"}
        for name in names
    ]
    dest = data_dir / "live_directory_staging.csv"
    dest.write_text(rendered_csv(SIGHTING_FIELDS, rows), encoding="utf-8")
    return {"staging_path": str(dest), "headings": len(rows), "status": "unverified_web_sightings"}

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument("--check", action="store_true", help="Fail if staged source sightings are absent from candidates")
    choice.add_argument("--write", action="store_true", help="Add only missing discovered candidates")
    choice.add_argument("--fetch-czechstartups", action="store_true", help="Fetch public HTML to separate staging CSV (not a database)")
    args = parser.parse_args()
    if args.fetch_czechstartups:
        print(json.dumps(fetch_directory_staging(), indent=2))
        return 0
    candidates = load_rows(DATA / "candidates.csv")
    sightings = load_rows(DATA / "discovery_sightings.csv")
    merged, additions, duplicates = merge(candidates, sightings)
    result = {
        "source_sightings": len(sightings), "existing_candidates": len(candidates),
        "missing_candidates": len(additions), "matched_existing_or_duplicates": len(duplicates),
        "final_candidates_if_written": len(merged),
        "note": "Source mentions are NOT direct-investment verification"
    }
    if args.write and additions:
        (DATA / "candidates.csv").write_text(rendered_csv(CANDIDATE_FIELDS, merged), encoding="utf-8")
        result["written"] = len(additions)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if args.check and additions else 0

if __name__ == "__main__":
    raise SystemExit(main())
