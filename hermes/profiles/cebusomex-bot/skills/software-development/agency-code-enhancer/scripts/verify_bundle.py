"""Offline integrity and analysis-coverage checks; never execute upstream code."""
from pathlib import Path
import hashlib
import json
import sys


def verify(base):
    meta = json.loads((base / 'references/provenance.json').read_text())
    root = base / 'assets/upstream'
    expected = {x['path']: x for x in meta['files']}
    actual = {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()}
    assert actual == set(expected), 'Source file coverage mismatch'
    assert len(actual) == meta['file_count'], 'Declared source total mismatch'
    for rel, record in expected.items():
        blob = (root / rel).read_bytes()
        assert len(blob) == record['bytes'], f'Size mismatch: {rel}'
        assert hashlib.sha256(blob).hexdigest() == record['sha256'], f'Hash mismatch: {rel}'
    catalog = (base / 'references/catalog.md').read_text()
    assert len(meta['agents']) == meta['agent_count']
    assert len({a['path'] for a in meta['agents']}) == meta['agent_count']
    for agent in meta['agents']:
        assert agent['path'] in expected, f'Missing agent {agent}'
        assert 'assets/upstream/' + agent['path'] in catalog, f'Agent not cataloged: {agent}'
    coverage = json.loads((base / 'references/review-coverage.json').read_text())
    assert set(coverage['reviewed_files']) == actual, 'Reviewed source file coverage mismatch'
    assert set(coverage['reviewed_folders']) == set(meta['folder_counts']), 'Reviewed folder coverage mismatch'
    analysis = (base / 'references/folder-analysis.md').read_text()
    for folder in meta['folder_counts']:
        assert f'`{folder}`' in analysis, f'Folder missing from analysis: {folder}'
    assert (root / 'LICENSE').read_text().startswith('MIT License')
    skill = (base / 'SKILL.md').read_text()
    assert skill.startswith('---\n') and '\n---\n' in skill[4:]
    assert 'name: agency-code-enhancer' in skill
    for section in ['## When to Use', '## Procedure', '## Pitfalls', '## Verification']:
        assert section in skill
    return {'status': 'PASS', 'source_files': len(actual), 'agents': len(meta['agents']),
            'folders': len(meta['folder_counts']), 'reviewed_files': len(set(coverage['reviewed_files'])),
            'commit': meta['commit']}


if __name__ == '__main__':
    try:
        print(json.dumps(verify(Path(__file__).resolve().parents[1]), indent=2))
    except (AssertionError, OSError, KeyError, ValueError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        sys.exit(1)
