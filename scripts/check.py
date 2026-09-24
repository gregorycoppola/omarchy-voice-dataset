#!/usr/bin/env python3
"""Validate the current catalog independently of historical source hashes."""
from export_catalog import export, ROOT
from intent_explorer import IntentExplorer

export(check=True)
explorer = IntentExplorer.load(ROOT)
assert len(explorer) == 223
assert sum(1 for _ in explorer.iter_pairs()) == 2230
for sequence in explorer.iter_sequences():
    explorer.catalog.validate_plan([
        {'intent': step.intent, 'arguments': step.arguments, **({'id': step.id} if step.id else {})}
        for step in sequence.steps])
print(f'OK: {len(explorer)} structured intents, 2230 labeled examples and templates, '
      f'{sum(1 for _ in explorer.iter_sequences())} validated sequences')
print('Historical source identity is checked separately by scripts/check_source_snapshot.py.')
