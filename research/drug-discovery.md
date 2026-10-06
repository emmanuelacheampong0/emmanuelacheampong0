# Research brief: uncertainty-aware compound prioritization

**Status:** scoping proposal. No dataset has been modeled, and no experimental results are claimed.  
**Area:** machine learning, computational drug discovery, evaluation, uncertainty communication.

## The question

For one small-molecule activity prediction task from a public benchmark, how do scaffold-based data splits and a simple probability-calibration method change (1) predictive performance and (2) the quality of confidence estimates used to prioritize compounds?

This narrows the broad idea of “AI + drug production” to a feasible undergraduate computational study. It focuses on an early research decision—what to inspect next—rather than claiming to discover, manufacture, or recommend a medicine.

## Why this question

Machine-learning models can appear strong when test compounds closely resemble training compounds. MoleculeNet describes scaffold splitting as a more demanding split because it separates structurally distinct molecular frameworks. The Therapeutics Data Commons organizes public tasks and datasets across therapeutic discovery and development. These resources make it possible to study evaluation choices reproducibly, while underscoring that a benchmark is only a simplified proxy for the real research pipeline.

## Proposed study

1. **Select one task.** After checking documentation, choose a public binary bioactivity task with manageable size, clear label definition, and permitted use (candidate: a TDC / MoleculeNet classification task).
2. **Audit the data.** Record source, version, units/thresholds, class balance, duplicate structures, missing labels, and scaffold counts. Preserve a reproducible data-preparation script.
3. **Set up comparisons.** Compare a simple majority or nearest-neighbor baseline and a transparent fingerprint-based classifier. If feasible, compare uncalibrated output with one post-hoc calibration method using a validation split.
4. **Compare splits.** Use random and scaffold-based splits with fixed seeds and report their construction. Do not tune on the held-out test partition.
5. **Evaluate.** Report ROC-AUC and PR-AUC for ranking, plus Brier score and a reliability diagram for probabilities. Consider a predeclared abstention/coverage analysis: when the model declines to rank low-confidence compounds, how do error and retained coverage change?
6. **Interpret conservatively.** Describe how split choice and calibration changed the evaluation in this benchmark. Do not present predictions as biological validation or medical guidance.

## Hypotheses to test

- **H1:** Scaffold-based evaluation will be more challenging than a random split for at least one of the chosen performance measures.
- **H2:** A calibration step may improve probability reliability on validation-like data, but it may not fully solve uncertainty under scaffold shift.
- **H3:** A confidence-aware review policy can expose trade-offs between the number of compounds retained and the error among those retained.

These are hypotheses, not findings.

## Measures and reporting

- Discrimination/ranking: ROC-AUC and PR-AUC, with class prevalence shown.
- Probability quality: Brier score and reliability plot, with calibration method and data split stated.
- Selective review: coverage and error/risk at predeclared confidence thresholds; report the policy and denominator.
- Robustness: repeated fixed seeds or repeated scaffold splits if supported by the dataset and time.
- Reproducibility: environment/version notes, seed, preprocessing, split assignment, and a run command.

## Limitations and safeguards

Public assay datasets can contain measurement noise, inconsistent protocols, class imbalance, duplicate or related molecules, and historical sampling bias. Scaffold separation is a more demanding structural test but does not reproduce prospective laboratory work. Metrics depend on the task and threshold; calibration on a small validation set can itself be unstable. A single benchmark cannot establish usefulness across diseases, targets, or compounds. No wet-lab testing, safety assessment, clinical interpretation, or drug-development claim is part of this project.

## Next steps

1. Read the benchmark papers and dataset cards.
2. Confirm task definition, dataset availability, and licensing.
3. Ask a faculty mentor to review feasibility and chemistry assumptions.
4. Write a short preregistered analysis plan before modeling.
5. Build the smallest reproducible baseline; document the limitations before expanding scope.

## Starting references

- Wu, Z. et al. (2018). [MoleculeNet: a benchmark for molecular machine learning](https://doi.org/10.1039/C7SC02664A). *Chemical Science*, 9, 513–530. Introduces benchmark tasks and discusses data splitting, including scaffold splits.
- Huang, K. et al. (2021). [Therapeutics Data Commons: Machine Learning Datasets and Tasks for Drug Discovery and Development](https://arxiv.org/abs/2102.09548). NeurIPS Datasets and Benchmarks. Describes a common framework for therapeutic ML datasets and tasks.
- Therapeutics Data Commons. [Official project and task documentation](https://tdcommons.ai/).
- Landrum, G. et al. [RDKit documentation](https://www.rdkit.org/docs/) (if RDKit is selected for structure parsing and scaffold generation; implementation details must be verified against the installed version).

## Notebook entry template

For each future experiment, record: date; question; source/version; exact split; model; seed; metrics; plots; unexpected behavior; limitations; what changed in the next iteration. Keep the raw result separate from interpretation.
