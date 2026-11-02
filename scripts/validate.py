#!/usr/bin/env python3
"""Agent Sentinel - automated validation.

Checks:
  1. All data/*.json files are valid JSON with required top-level keys.
  2. mkdocs build succeeds (invoked separately by the build script).
  3. Internal documentation links resolve against the docs tree.

Exit code 0 = pass, non-zero = fail.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT, "data")
DOCS_DIR = os.path.join(ROOT, "docs")

REQUIRED_KEYS = {
    "research-state.json": ["schema_version", "last_updated", "site_version", "operating_mode"],
    "sources.json": ["schema_version", "sources"],
    "claims.json": ["schema_version", "claims"],
    "frameworks.json": ["schema_version", "frameworks"],
    "regulations.json": ["schema_version", "regulations"],
    "controls.json": ["schema_version", "controls"],
    "threats.json": ["schema_version", "threats"],
    "incidents.json": ["schema_version", "incidents"],
    "tools.json": ["schema_version", "tools"],
    "vendors.json": ["schema_version", "vendors"],
    "evaluations.json": ["schema_version", "evaluations"],
    "glossary.json": ["schema_version", "glossary"],
    "jurisdiction-matrix.json": ["schema_version", "jurisdictions"],
    "control-crosswalks.json": ["schema_version", "crosswalks"],
    "update-history.json": ["schema_version", "update_history"],
    "vulnerabilities.json": ["schema_version", "vulnerabilities"],
    "vulnerability-products.json": ["schema_version", "vulnerability_products"],
    "vulnerability-aliases.json": ["schema_version", "vulnerability_aliases"],
    "vulnerability-history.json": ["schema_version", "vulnerability_history"],
    "remediation-actions.json": ["schema_version", "remediation_actions"],
    "vulnerability-state.json": ["schema_version", "vulnerability_state"],
}

errors = []


def check_json_files():
    for fname, keys in REQUIRED_KEYS.items():
        path = os.path.join(DATA_DIR, fname)
        if not os.path.exists(path):
            errors.append(f"MISSING data file: {fname}")
            continue
        try:
            with open(path) as f:
                obj = json.load(f)
        except json.JSONDecodeError as exc:
            errors.append(f"INVALID JSON in {fname}: {exc}")
            continue
        for key in keys:
            if key not in obj:
                errors.append(f"MISSING key '{key}' in {fname}")


# Collect doc markdown files and their link targets
def collect_docs():
    markdown_files = []
    for root, _, fl in os.walk(DOCS_DIR):
        for f in fl:
            if f.endswith(".md"):
                markdown_files.append(os.path.join(root, f))
    return markdown_files


def check_links():
    pages = collect_docs()
    # Build a set of resolvable targets: directories (index) and files
    targets = set()
    for root, dirs, fl in os.walk(DOCS_DIR):
        for d in dirs:
            targets.add(os.path.relpath(os.path.join(root, d), DOCS_DIR))
        for f in fl:
            relf = os.path.relpath(os.path.join(root, f), DOCS_DIR)
            targets.add(relf)
            if f == "index.md":
                targets.add(os.path.relpath(root, DOCS_DIR))

    md_link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for md in pages:
        rel = os.path.relpath(md, DOCS_DIR)
        with open(md) as f:
            content = f.read()
        base_dir = os.path.dirname(rel)
        for match in md_link_re.findall(content):
            raw = match.split("#")[0].split("?")[0].strip()
            if not raw or raw.startswith(("http://", "https://", "mailto:")):
                continue
            if raw.startswith("/"):
                target = raw.lstrip("/")
            else:
                # relative to the source file's directory
                target = os.path.normpath(os.path.join(base_dir, raw))
            if target.endswith(".md"):
                if target not in targets:
                    errors.append(f"BROKEN LINK in {rel}: -> {raw}")
            else:
                # directory target resolves to <dir>/index.md
                if target in targets:
                    continue
                if (target + ".md") not in targets and (target + "/index.md") not in targets:
                    errors.append(f"BROKEN LINK in {rel}: -> {raw}")


def main():
    check_json_files()
    check_links()
    if errors:
        print("VALIDATION FAILED:")
        for e in errors:
            print("  - " + e)
        print(f"Found {len(errors)} error(s).")
        return 1
    print("VALIDATION PASSED: all JSON schema checks and internal links OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
