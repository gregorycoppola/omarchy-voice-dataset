#!/usr/bin/env python3
"""Generate compatibility/browser views from catalog.json; never author these views."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from intent_explorer.catalog import Catalog


def payloads():
    catalog = Catalog(ROOT)
    historical = json.loads((ROOT / 'data/history/2026-09-24/intents.json').read_text())
    support = {row['id']: row['support'] for row in historical['intents']}
    rows = []
    for definition in catalog.intents.values():
        row = {key: value for key, value in definition.items() if key not in ('examples', 'grammar')}
        row['slots'] = definition['arguments_schema']['properties']
        row['examples'] = [{'text': e['text'], 'parsed': {'intent': e['intent'], 'arguments': e['arguments']}}
                           for e in definition['examples'] if e['variant'] <= 2]
        row['support'] = support.get(row['id'], {})
        rows.append(row)
    meta = {'schema_version': 2, 'catalog_revision': catalog.revision,
            'generated_from': 'catalog.json', 'status': 'schema_defined_not_execution_validation'}
    return {
        'outcomes.json': {**meta, 'outcomes': rows},
        'intents.json': {**meta, 'intents': rows},
        'utterances.json': {**meta, 'snapshot_date': '2026-09-24',
                           'entries': [e for d in catalog.intents.values() for e in d['examples']]},
        'llm-intents.schema.json': catalog.llm_schema(),
    }


def export(check=False):
    for name, value in payloads().items():
        text = json.dumps(value, indent=2, ensure_ascii=False) + '\n'
        path = ROOT / 'data' / name
        if check:
            if not path.is_file() or path.read_text() != text:
                raise ValueError(f'Stale generated view: {name}; run scripts/export_catalog.py')
        else:
            path.write_text(text)


if __name__ == '__main__':
    export('--check' in sys.argv)
    print('Validated catalog and generated views' if '--check' in sys.argv else 'Exported catalog views and LLM schema')
