# Contributing Guidelines

Welcome! We curate human activity and motion datasets with high editorial standards. Follow the steps below to propose new datasets, improve existing cards, or add tooling.

## Table of Contents
1. [Ground Rules](#ground-rules)
2. [Adding a Dataset](#adding-a-dataset)
3. [Updating an Existing Card](#updating-an-existing-card)
4. [Submitting Tooling or Docs](#submitting-tooling-or-docs)
5. [Style Notes](#style-notes)
6. [Review Checklist](#review-checklist)

## Ground Rules
- Be precise. Provide official links, paper citations, license terms, and version numbers.
- Respect licenses. If data requires application or special approval, note it clearly.
- Transparency only: do not mirror datasets without permission; always point to the original source.
- Keep tone neutral and factual. Avoid marketing language.
- Run validation helpers before opening a pull request (link checker, schema checks).

## Adding a Dataset
1. **Create or copy a card template**  
   - Use [`datasets/_template.md`](datasets/_template.md) as a starting point.  
   - Place the new file inside the appropriate modality folder (`vision/`, `wearable/`, `skeleton/`, `multimodal/`, or `emerging/`).
2. **Fill in required sections**  
   - Overview (modality, sensors, tasks, scale).  
   - Access & licensing (include application instructions if any).  
   - Reference paper(s) with BibTeX-ready citation.  
   - Baselines / benchmarks (minimum of one published baseline).  
   - Tooling & ecosystem (code repos, loaders, evaluation kits).  
   - Known challenges or caveats (class imbalance, annotation noise, etc.).
3. **Add to the taxonomy table**  
   - Update `README.md` to include the dataset with modality and quick facts.
4. **Validate**  
   - Run `tools/validate_links.ps1` (in development) or the GitHub Action output on your fork.  
   - Run `python tools/normalize_ascii.py --dry-run` to ensure no unintended Unicode slips in.  
   - Ensure Markdown passes `markdownlint` (recommended).
5. **Open a pull request**  
   - Use the "Dataset addition" PR template.  
   - Fill in the checklist and provide context on why the dataset matters.

## Updating an Existing Card
- Keep change scope focused; if you are fixing multiple datasets, split into separate commits.
- Include references when updating baseline numbers or SOTA claims (conference, leaderboard).
- If a link is dead, provide a working alternative and explain the change in your PR.
- Flag major licensing changes in the PR description so reviewers can highlight it in release notes.

## Submitting Tooling or Docs
- Place scripts in `tools/` with clear CLI usage and docstrings.
- Provide minimal reproduction steps or tests when adding automation.
- Documentation additions belong in `docs/` (surveys, comparisons, design notes) unless tightly coupled with a dataset card.
- Localization files live in `i18n/`. When starting a translation, copy the language-switch banner, keep relative links working, and add yourself as a contributor in the PR description.

## Style Notes
- Prefer American English spelling for consistency (e.g., "modeling").
- Use present tense and active voice.
- Tables should be GitHub-compatible Markdown.
- Keep paragraphs under four sentences; use bullet lists for dense facts.
- Link to DOI or arXiv when possible (`https://doi.org/...` or `https://arxiv.org/abs/...`).

## Review Checklist
Reviewers confirm the following before merging:
- [ ] Dataset card uses the template and required headings.
- [ ] All external links resolve (no HTTP errors).
- [ ] Licensing terms are documented and non-conflicting.
- [ ] Baseline metrics cite a published source or official leaderboard.
- [ ] README taxonomy table updated (if applicable).
- [ ] Tests / validation scripts (if touched) run successfully.
- [ ] PR title follows `<type>: <summary>` convention (e.g., `dataset: add BABEL v1.0`).

Thank you for making this catalog better for the community! Reach out via GitHub Discussions for questions or to propose larger initiatives.
