# Verification record — 2026-09-24

| Project | Check run | Result | Scope |
| --- | --- | --- | --- |
| Skipper | `python -m unittest discover -s tests -p 'test_grammar.py' -q` | 8 passed | Grammar tests only; source checkout has uncommitted edits. |
| Genesis | `bash tests/intent.sh` | 163 passed, 0 failed | Phrase-to-action parser; the action executor and external plugins were not run. |
| Omarvis | `python -m pytest -q tests/test_catalog.py tests/test_policy.py` | Not run: `pytest` absent from system Python and the shared Skipper venv | Catalog and policy modules imported to enumerate routes; no test suite or live session result. |
| OMA | `python -m unittest discover -s tests -p 'test_discovery.py' -q` | 22 passed | Mocked discovery behavior. |
| OMA | `python -m unittest discover -s tests -p 'test_policy.py' -q` | 29 passed, 1 failed | The failing `test_unknown_action_lists_the_real_ones` expects a `google-chrome` desktop entry with `new-window`; this machine has no matching entry. This is an environment-dependent failure, not proof of a broken tool or a successful voice pipeline. |
| Omause | `npm ci --ignore-scripts --no-audit --no-fund --silent`; `npm test -- --test-reporter=dot` | 157 passed, 0 failed | Local unit tests and mocked execution paths; no TypeSafe API call or voice pipeline. |
| OmaPilot | `npm ci --ignore-scripts --no-audit --no-fund --silent`; `npm test -- runtime/test/desktop-tools.test.ts runtime/test/capability-tools.test.ts` | 12 passed, 1 skipped | Two targeted tool test files; no provider session or connected account action. |
| Handy plugin | `bash tests/run` | All eleven temporary-home shell test scripts passed | Fake commands and temporary user directories; real Handy dictation was not tested. |
| OmaYap | `bash tests/run` | All bundled tests passed | Fake Piper voice and audio sink; real playback was not tested. |
| Voxtype Enhance | `python -m unittest discover -s tests -q` | 24 passed | Voxtype configuration bridge with mocks; no real model download or dictation. |
| omarchy-stt, Voxtype, Voice Input | No test suite run | Source inventory only | Models and installed services were not set up in this research workspace. |
| Installed Omarchy | `omarchy version`; `omarchy commands --json` | Version `4.0.3-1`, 387 public routes captured | Read-only CLI metadata; no route action was executed. |

All eleven external source checkouts were clean at their pinned commits. This
record tests **selected source behavior**, not installation, microphone input,
model interpretation, provider access, plugin dependencies, or action results.
The newer eight project inventories are targeted source reviews. Dynamic routes,
user-defined tools, and optional accounts remain environment dependent; the
crosswalk does not assert they were exercised.
