# Research State

This page tracks research and vulnerability discovery cut-offs for the site. The
authoritative machine-readable state is in `data/research-state.json`.

!!! note "Operating mode"
    The site is currently in **Incremental Reconciliation** mode, applying delta changes since
    the last successful run (2026-11-02).

## Current state

| Field | Value |
|-------|-------|
| **Site version** | 1.1.0 |
| **Research cutoff** | 2026-11-04 |
| **Vulnerability cutoff** | 2026-11-04 |
| **Previous research cutoff** | 2026-11-02 |
| **Previous vulnerability cutoff** | 2026-11-02 |
| **Last successful run** | 2026-11-04 |
| **Operating mode** | incremental |

## Why cutoffs matter

Cut-offs define the **delta** for each reconciliation run:

- Content published **after** the research cutoff is candidate material for the next run.
- New vulnerabilities and revised advisories are assessed against the active set.
- Cut-offs advance **only after** validation succeeds (see [Run Reports](run-reports.md)).

## Reconciliation trigger

Perform a **full reconciliation** (not just incremental) when the incremental process may
have missed: delayed identifiers, revised advisories, changed regulations, revised framework
mappings, rejected/disputed vulnerabilities, newly exploited older vulnerabilities,
corrected affected-version ranges, new fixes, provider advisories without CVEs, or aliases
added after initial publication.

## Claim traceability

Claims on this site are traced to sources in `data/claims.json` and `data/sources.json`.
Distinguish clearly between **sourced fact**, **technical observation**, **inference**, and
**recommendation** — this site never represents technical guidance as legal advice.
