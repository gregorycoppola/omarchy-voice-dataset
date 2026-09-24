# Parsing strategies to compare

Version 2 now defines structured schemas for all 223 intents. See
[the current model and workflow](structured-intents.md). Historical counts and
example lists below describe the original audit; use `data/catalog.json` and
the browser explorer for current definitions.

The [utterance set](utterance-variants.md) provides 2,230 illustrative phrases
for 223 candidate intent labels. Each intent has two authored illustrations
and eight closely related synthetic request frames. A parser that
does well on them has **not** demonstrated that it understands real speech or
that an app can execute the result. The 168 candidate intents also lack
reviewed argument schemas.

## Before benchmarking

1. Review overlapping labels. For example, `browser.tab_close` with an
   all-tabs target overlaps `browser.tabs_clear`; `app.close` and
   `browser.close` can refer to the same visible result. Set a clear expected
   label or allow more than one acceptable label for each ambiguous case.
2. Add argument schemas and representative values for the 168 candidates.
   Current `null` arguments mean "not labeled," not "no arguments."
3. Collect a small holdout of independently phrased or consented real
   transcripts. Keep it out of parser prompts, templates, and training data.
4. Group synthetic variants with their `base_variant` when splitting data.
   A random row split leaks the same core phrase into both train and test.
5. Include requests outside the catalog, incomplete commands, and phrases
   with multiple possible interpretations. A safe parser must be able to
   return `unknown` or ask for clarification.

## Candidate approaches

| Strategy | How it works | Main tradeoff to measure |
| --- | --- | --- |
| Grammar and slot rules | Match authored phrase patterns and extract typed values. | Predictable and fast; coverage depends on maintained patterns. |
| Lexical retrieval | Rank example phrases using normalized words or character n-grams. | Simple baseline; vulnerable to wording changes and near-duplicate intents. |
| Embedding retrieval | Rank intent examples by semantic similarity, then extract slots separately. | Handles paraphrases; thresholds and overlapping intents need calibration. |
| Structured language model | Ask for an intent ID and arguments under a constrained schema. | Flexible; adds cost, latency, and possible unsupported guesses. |
| Hybrid | Try precise rules first, then retrieval or model inference, with a final validation and abstention step. | Extra system complexity; may improve coverage without losing exact commands. |

Run each strategy on the same held-out inputs. Record top intent accuracy,
argument accuracy, abstention on unsupported requests, ambiguity handling,
latency, and cost. Report results by intent family and by source of phrasing
(authored text versus real transcript). Parser output should stop at an intent
record during evaluation; execution and authorization are separate stages.

For [command sequences](command-sequences.md), also score clause boundaries,
ordered intent lists, reference bindings such as “it,” and whether a source
macro was selected only when its exact behavior matches the request. Keep
standalone command examples and composed sequence examples in separate test
slices so a parser cannot gain credit from near-duplicate wording alone.

The source dataset proves neither parser accuracy nor end-to-end command
success. See [coverage](intent-coverage.md) and [verification](verification.md)
for the current evidence boundary.
