# Run Reports

Each site run produces a report documenting what was researched, what changed, what was
rejected, validation results, and cut-off advancement. Reports are stored in
`reports/runs/`.

## Run index

| Date | Version | Mode | Outcome | Report |
|------|---------|------|---------|--------|
| 2026-11-02 | 1.0.0 | First Run | Complete | [Run 001](https://github.com/govindsme/agentsentinel/blob/main/reports/runs/run-2026-11-02-v1.0.0.md) |
| 2026-11-04 | 1.1.0 | Incremental | Complete | [Run 002](https://github.com/govindsme/agentsentinel/blob/main/reports/runs/run-2026-11-04-v1.1.0.md) |

## What a run report contains

- Research and vulnerability cut-offs used.
- Candidate changes identified and their **classification**
  (added / updated / consolidated / archived / rejected / deleted).
- Validation results (build, link check, data schema checks).
- Cut-off advancement decision.
- Unresolved questions and evidence gaps.

## How runs are tracked

- Previous cut-offs always come from the **last successful run**.
- Cut-offs advance **only after** validation succeeds.
- Candidate changes are applied **only when supported** by trustworthy evidence.

For the chronological change log, see [Update History](update-history.md).
