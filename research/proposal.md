# Designing AI Budgeting Tools Students Can Question

## The role of explanations, evidence, and reflection prompts in calibrated reliance

**Research proposal · October 2026 · Project owner: Emmanuel Sefah Acheampong**

> This document proposes a study and prototype. It reports no participant data, results, or completed research.

## Abstract

Generative AI is appearing in products that help people plan, learn, and make decisions. A useful AI product needs more than a persuasive answer: people need a way to judge when its recommendation fits their situation and when it does not. This proposal studies that product-design challenge through fictional college-budget scenarios. It asks whether a structured recommendation card—with an explanation tied to the scenario, visible evidence, a concise limitation, and a prompt to check a key assumption—helps students distinguish sound advice from advice that conflicts with the facts. A proposed randomized, between-subjects pilot would compare that card with a plain-text recommendation while keeping the underlying recommendations identical. The study would measure decision accuracy, appropriate reliance, confidence calibration, comprehension, and perceived effort. The prototype would use fixed, researcher-authored recommendations rather than a live language model so the content is stable and the interface is the factor under examination. The work is intended to produce an evidence-informed product direction and a transparent research artifact, not financial guidance. Any study with people would proceed only after instructor and institutional ethics review.

## 1. Background and motivation

AI features increasingly sit inside everyday products as assistants, copilots, recommenders, and chat interfaces. Product teams are often rewarded when people use a feature, return to it, or say they trust it. Yet trust by itself is not a sufficient success measure. A person can trust a correct recommendation for a good reason, follow an incorrect recommendation, reject useful advice, or make a correct decision without understanding why. A responsible product should help users make good decisions and retain agency when the system is uncertain or wrong.

This problem is especially interesting in a financial-wellness setting. Students encounter choices about saving, bills, books, transportation, and discretionary spending, but a study should not ask them to expose personal financial information or follow real financial advice. Fictional cases provide a safer way to examine how a product interface shapes judgment. The proposed tasks use only invented people, amounts, and constraints; there is no investment guidance, account connection, or collection of participants’ budgets.

The project brings together four interests:

- **AI and software engineering:** implement a controlled, testable prototype with fixed system outputs.
- **Product management:** define the user problem, success metrics, product trade-offs, and a validation roadmap.
- **Product and interaction design:** test how explanations, evidence, limitations, and a reflection step affect the decision experience.
- **FinTech:** use a familiar financial-wellness context while keeping the study educational, fictional, and low risk.

## 2. Problem statement and research gap

AI explanations can change whether people follow a system, but an explanation is not automatically useful. In a 2025 CHI controlled experiment, Kim and colleagues found that explanations increased reliance on both correct and incorrect LLM responses; sources and inconsistencies reduced reliance on incorrect responses in their task. Vasconcelos and colleagues found that people’s effort to inspect explanations matters: making verification easier can reduce overreliance. Schemmer and colleagues define appropriate reliance in terms of accepting correct AI advice and rejecting incorrect AI advice, rather than simply maximizing trust or adoption.

These findings suggest a product question: can a carefully designed interface make the basis and limits of a recommendation easier to inspect in a student budgeting task? The current proposal does not claim that the proposed interface will work. It tests a plausible design hypothesis. It also separates the interface effect from model quality by holding the recommendation text and correctness constant across conditions.

## 3. Research question and objectives

### Primary question

**When college students evaluate fictional budgeting recommendations, does a structured AI recommendation card help them make more accurate decisions and rely on the system more appropriately than plain-text recommendations?**

### Secondary questions

1. Does the structured card improve confidence calibration—confidence that is higher for correct decisions than for incorrect ones?
2. Do students understand which scenario facts support or conflict with a recommendation?
3. Does the additional interface information increase perceived effort or make the task feel clearer?
4. Which part of the experience do students say they would keep, change, or remove?

### Objectives

1. Build a small, accessible prototype with two controlled presentation conditions.
2. Create fictional budgeting cases with recommendations that can be independently checked against explicit constraints.
3. Pilot a study protocol and measures that distinguish trust, reliance, decision quality, confidence, and effort.
4. Turn the findings—if the study is approved and completed—into product requirements and a prioritized next experiment.

## 4. Study hypotheses

- **H1:** Participants assigned to the structured card will achieve higher decision accuracy than participants assigned to plain text.
- **H2:** Participants assigned to the structured card will show greater appropriate reliance: more acceptance of recommendations that satisfy the stated constraints and more rejection of recommendations that violate them.
- **H3:** The structured card will improve confidence calibration, measured as the relationship between confidence and correctness, not simply raise average confidence.
- **H4:** The structured card may increase perceived effort because it invites inspection; whether the extra effort is acceptable will be treated as a product trade-off, not automatically a failure.

This is an exploratory student pilot. H1–H4 are predictions, not findings. A confirmatory study would need a power analysis based on pilot estimates and a preregistered plan.

## 5. Product concept and design

The prototype presents the same short “AI budgeting suggestion” in both conditions.

| Condition | What the participant sees |
|---|---|
| **A — Plain text** | A concise recommendation in a simple text block, followed by the fictional scenario and accept/reject choice. |
| **B — Structured card** | The same recommendation, plus (1) a short explanation linked to a stated scenario fact, (2) the evidence used, (3) one relevant limitation or missing detail, and (4) a neutral prompt: “Which detail would you check before deciding?” |

The system’s recommendation, whether it is correct, and the task content remain identical between conditions. Only the presentation changes. This tests the combined card design; it cannot isolate the effect of each component. If it shows promise, a later factorial or component test can separate the explanation, evidence, limitation, and reflection prompt.

### Product principles

- **Show the basis:** connect a recommendation to facts the person can inspect.
- **Make uncertainty useful:** name relevant missing information instead of displaying a decorative confidence percentage.
- **Invite judgment:** make accepting, rejecting, and editing the suggestion equally visible.
- **Keep the person in control:** the interface supports a decision; it does not make or execute one.
- **Design for comprehension:** use plain language, readable contrast, keyboard access, and responsive layouts.

### Product success metric

The primary product metric is **decision quality on constraint-checkable cases**, not clicks, time-on-screen, stated trust, or feature adoption alone. Secondary product measures include appropriate reliance, calibration, comprehension, and perceived effort. A design that raises acceptance but also raises acceptance of incorrect recommendations would not count as a successful result.

## 6. Proposed method

### Design

A randomized, between-subjects usability experiment with two interface conditions. Each participant sees one condition only, which avoids learning the interface contrast before responding. The prototype will use scripted, researcher-authored outputs; it will not call an LLM. This keeps the wording and error pattern fixed and lets the study examine the interface rather than changes in model behavior.

### Participants and recruitment

The proposed pilot population is adult undergraduate students, recruited through an instructor-approved campus channel only after an institutional review determination. A practical pilot target is **40–60 participants**, split approximately evenly between conditions. This number is for usability and feasibility estimation, not a claim of adequate statistical power or a representative sample. Recruitment criteria, compensation if any, and final sample size must be set with the instructor and IRB before recruitment.

### Materials

Participants would review eight short fictional cases, each with a small budget table, a stated goal or constraint, and an AI-style recommendation. Four recommendations would satisfy the case constraints and four would violate a clearly stated constraint. A reviewer with relevant financial-literacy or teaching expertise should audit the cases before use. Cases would be matched for reading length and difficulty. The interface condition would not reveal the correctness label.

For each case, the participant would:

1. Read the fictional situation and the recommendation.
2. Choose **accept**, **reject**, or **edit the suggestion**.
3. Rate decision confidence from 1 (“not at all confident”) to 5 (“very confident”).
4. Answer one brief comprehension check about the stated constraint.

After the cases, participants would complete a short perceived-effort rating and open-ended questions about what helped, confused, or felt unnecessary. A short background form could ask year of study and prior experience with AI tools, but it would not ask income, debt, account details, or personal spending.

### Example task

“Jordan has $120 left after listed essentials. Jordan needs to keep at least $45 for a required course lab fee due tomorrow. The AI suggests using the full $120 for an optional purchase today.” Participants decide what to do. The correct evaluation follows from the explicit constraint: the suggestion conflicts with the stated need to reserve $45. This is a fictional reasoning task, not advice for a participant’s finances.

### Procedure

1. Provide an information sheet and obtain voluntary consent after approval.
2. Explain that the AI is simulated, recommendations can be wrong, every situation is fictional, and the activity is not financial advice.
3. Randomly assign a participant to Condition A or B.
4. Present a short practice example, followed by eight balanced cases in randomized order.
5. Collect accept/reject/edit decisions, confidence ratings, and comprehension answers for each case.
6. Collect the effort rating and open-ended feedback.
7. Debrief participants and provide contact information for the researcher and instructor/ethics contact.

The proposed session length is 15–20 minutes. Participation is voluntary; participants can skip a question or stop without penalty.

## 7. Measures and analysis plan

### Primary outcome: decision accuracy

For each case, score the participant’s choice against a case rubric established before data collection. Accepting a constraint-consistent recommendation or rejecting/editing a constraint-violating one is scored as correct. The rubric must explicitly define how “edit” is scored for each case. Report accuracy by condition with uncertainty intervals.

### Appropriate reliance

Report the two parts separately: (a) acceptance of correct recommendations and (b) rejection or appropriate modification of incorrect recommendations. Also report their combined balanced score. This avoids treating blanket acceptance or blanket rejection as good reliance.

### Confidence calibration and comprehension

Compare confidence with correctness at the case level. Report calibration descriptively and, if the sample supports it, estimate whether confidence distinguishes correct from incorrect judgments. Comprehension is the proportion of constraint checks answered correctly. Self-reported trust is secondary and will not stand in for decision quality.

### Effort and qualitative feedback

Summarize perceived effort by condition. Code open-ended comments using a small, documented codebook (e.g., clarity, evidence usefulness, uncertainty, control, visual hierarchy, cognitive load). Have a second reviewer independently code a subset and resolve differences transparently if available.

### Statistical approach

Before recruitment, preregister the hypotheses, exclusions, scoring rubric, and analysis. For a small pilot, prioritize group summaries, effect sizes, confidence intervals, missingness, and task usability. If the final sample permits, fit a mixed-effects logistic model for case-level correctness with interface condition as a fixed effect and participant and case as random intercepts. Do not claim causal generalization from a small convenience sample. Report null or mixed results and deviations from the plan.

## 8. Ethics, privacy, and risk management

No recruitment, interviews, or data collection should begin until the instructor and Elon University’s appropriate human-subjects/IRB office determine the review pathway and approve or exempt the project as appropriate. A classroom project is not automatically exempt from review.

The study uses synthetic scenarios only. It will not request personal financial histories, bank credentials, health information, immigration status, or identifiable budget data. The prototype stores no responses and sends no information to a server. If a later study needs data storage, the researcher must use an approved, access-controlled location, collect only necessary fields, remove direct identifiers, state a retention/deletion schedule, and update consent materials. Participants will be told the recommendations are simulated and can be wrong. The task will not ask them to act on suggestions in real life.

Potential risks include mild discomfort about money-related examples and confusion about whether the product provides advice. The study will use neutral wording, allow skipping and withdrawal, explicitly label cases as fictional, and debrief participants. These steps reduce risk but do not replace an ethics review.

## 9. Limitations

- A small campus convenience sample will not represent all students or financial situations.
- Fixed recommendations isolate interface design but do not capture the variability of a live LLM.
- Constraint-checkable cases are simpler than real financial decisions and may overstate the ease of detecting errors.
- The proposed structured card changes several design elements together; a positive effect cannot identify which element caused it.
- Short-term choices do not measure learning, long-term trust, or real-world financial outcomes.
- Self-reported trust and effort can be affected by social desirability and participants’ interpretations of the questions.

The appropriate claim after a pilot would be about feasibility and observed patterns in the tested prototype and cases—not proof that AI budgeting products are safe or that the design generalizes broadly.

## 10. Expected contribution and product roadmap

The expected contribution is a documented prototype and a small, replicable study plan that makes product quality measurable beyond “users trusted it.” The project can inform interface requirements such as attaching evidence to claims, highlighting missing information, keeping user choices visible, and evaluating whether the system helps people reject errors.

### Roadmap

1. **Now — Scope and prototype:** finalize cases, accessibility basics, response controls, and test logic.
2. **Before any user study — Review:** seek faculty feedback, validate scenarios, complete the IRB process, and preregister.
3. **Pilot — Learn:** run only the approved study, inspect task comprehension and feasibility, then report all outcomes honestly.
4. **Next — Improve:** use feedback to revise the card and test individual components or a broader participant group with a power analysis.
5. **Later — Engineering:** if justified, prototype a real model integration with content provenance, uncertainty handling, privacy controls, and model-error monitoring as separate evaluated requirements.

## 11. Proposed timeline

| Stage | Work | Output |
|---|---|---|
| 1 | Review related research and define task rubric | Literature notes and preregistration draft |
| 2 | Build and accessibility-check prototype | Working local demo |
| 3 | Expert review of fictional cases and faculty/IRB review | Revised study materials and approval decision |
| 4 | Pilot only if approved | De-identified dataset and analysis log |
| 5 | Analyze, reflect, and revise product | Short research report and product recommendations |

## References

Kim, S. S. Y., Vaughan, J. W., Liao, Q. V., Lombrozo, T., & Russakovsky, O. (2025). Fostering appropriate reliance on large language models: The role of explanations, sources, and inconsistencies. *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3706598.3714020

Schemmer, M., Kühl, N., Benz, C., Bartos, A., & Satzger, G. (2023). Appropriate reliance on AI advice: Conceptualization and the effect of explanations. *Proceedings of the 28th International Conference on Intelligent User Interfaces*. https://doi.org/10.1145/3581641.3584066

Vasconcelos, H., Jörke, M., Grunde-McLaughlin, M., Gerstenberg, T., Bernstein, M. S., & Krishna, R. (2023). Explanations can reduce overreliance on AI systems during decision-making. *Proceedings of the ACM on Human-Computer Interaction, 7*(CSCW1), 1–38. https://doi.org/10.1145/3579605

## Research integrity note

This is a proposed undergraduate research direction written to support learning and project planning. The proposal and prototype were prepared with AI-assisted drafting and coding at Emmanuel’s direction. The references are starting points, not an exhaustive literature review. Emmanuel should read the complete papers, verify citation formatting, and refine the review with a faculty mentor before submission or recruitment. No results are fabricated or implied.
