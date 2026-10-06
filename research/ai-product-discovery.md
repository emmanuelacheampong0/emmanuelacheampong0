# Research direction: AI-assisted product discovery that keeps user context

**Status:** question development. No interviews, participant study, or results are claimed.

## Research question

How should an AI-assisted feedback synthesis interface help a product team identify recurring needs while preserving source evidence, low-frequency perspectives, and uncertainty?

## Why it matters

Product teams often work with feedback from different channels and with uneven detail. Automated clustering or summaries may reduce reading effort, but can make tentative patterns look settled or hide the people represented by only one or two comments. A useful product should help the team inspect the evidence behind a theme and notice disagreement before prioritizing a feature.

## Proposed product concept

A small interface that organizes a fixed, public or synthetic feedback corpus into candidate themes. Each theme would link to the original excerpts, show how many items support it, flag contradictory examples and low-frequency themes, and let a human editor rename, split, merge, or reject it. The interface would label machine-generated suggestions as suggestions and avoid claiming that mention frequency equals importance.

## Questions to investigate

- Do source links and evidence counts help users verify an AI-generated theme?
- Do explicit dissent and low-frequency views change what a participant chooses to prioritize?
- Which explanation is easier to inspect: a short rationale, examples, or an evidence map?
- How should the interface communicate that themes depend on corpus selection and model behavior?

## Possible prototype comparison

Compare two mock product-discovery interfaces using the same small, consent-safe corpus: a concise theme summary, and a source-linked evidence view that additionally exposes dissent and uncertainty. Begin with a heuristic walkthrough and task-based usability sessions only after an instructor reviews the plan. If people are recruited or data are collected, obtain an institutional IRB determination/approval before starting.

## Measures to consider

- Accuracy of identifying which original excerpts support a theme.
- Ability to notice a contradictory or low-frequency need.
- Confidence calibration: whether confidence matches evidence quality.
- Perceived usefulness and cognitive effort, interpreted alongside observed task performance.
- Qualitative reasons participants accept, edit, or reject a suggested theme.

## Risks and limitations

Synthetic or public feedback may not represent real product users. A small formative study would not establish broad causal effects. Frequency can be mistaken for importance; a system can reflect biases in data collection, language, and model behavior. The interface should not present a machine-generated summary as a user’s voice. Keep the source context visible and make human review meaningful.

## Next steps

1. Read primary HCI and human-AI interaction work on explanation, contestability, and mixed-initiative systems.
2. Select a small, ethically appropriate example dataset or create clearly labeled synthetic comments.
3. Draw two low-fidelity interface variants and define a short verification task.
4. Ask an instructor or mentor to review the research question, accessibility, and IRB requirements.
5. Publish the prototype and analysis plan before collecting any participant data.

## Research log

No study has been run. Update this file as sources are reviewed, design decisions are made, and the scope changes. Separate notes from observations and findings.
