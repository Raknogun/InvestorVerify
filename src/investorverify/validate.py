"""Validate candidate/evidence CSV consistency; not factual truth."""
import csv
from pathlib import Path
from urllib.parse import urlparse

REQUIRED_CANDIDATE = {'name', 'country', 'category_proposed', 'discovery_source_url', 'status'}
REQUIRED_EVIDENCE = {'investor_name', 'field', 'value', 'source_url', 'accessed_date', 'verification_status'}

def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))

def is_public_url(value: str) -> bool:
    parsed = urlparse(value)
    return parsed.scheme == 'https' and bool(parsed.hostname) and parsed.hostname not in {'localhost', '127.0.0.1'}

def validate(data_dir: Path) -> list[str]:
    candidates = read_csv(data_dir / 'candidates.csv')
    evidence = read_csv(data_dir / 'evidence.csv')
    errors: list[str] = []
    if not candidates: errors.append('No candidates')
    if not evidence: errors.append('No evidence')
    for filename, rows, fields in [('candidates', candidates, REQUIRED_CANDIDATE), ('evidence', evidence, REQUIRED_EVIDENCE)]:
        for index, row in enumerate(rows, 2):
            for field in fields:
                if not row.get(field, '').strip():
                    errors.append(f'{filename}.csv:{index}: missing {field}')
    names = [row['name'].strip() for row in candidates]
    if len(names) != len(set(names)): errors.append('Duplicate candidate names')
    for index, row in enumerate(candidates, 2):
        if not is_public_url(row['discovery_source_url']):
            errors.append(f'candidates.csv:{index}: invalid public URL')
    for index, row in enumerate(evidence, 2):
        if row['investor_name'] not in names: errors.append(f'evidence.csv:{index}: unknown investor')
        if not is_public_url(row['source_url']):
            errors.append(f'evidence.csv:{index}: invalid public URL')
    return errors

if __name__ == '__main__':
    root = Path(__file__).resolve().parents[2]
    problems = validate(root / 'data')
    for problem in problems: print('ERROR:', problem)
    print(f'Validation: {"FAIL" if problems else "PASS"} ({len(problems)} errors)')
    raise SystemExit(bool(problems))
