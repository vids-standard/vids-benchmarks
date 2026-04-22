#!/usr/bin/env python3
"""
Reproduce Table 4 from the VIDS compliance analysis paper (arXiv:2604.17525).

Reads per-dimension scores from data/compliance_scores.json and generates
the category-level summary table, per-category averages, and the 71% gap figure.

Usage:
    python verify_scores.py
    python verify_scores.py --json
"""

import json
import argparse
from pathlib import Path


def load_scores():
    path = Path(__file__).parent / "data" / "compliance_scores.json"
    with open(path) as f:
        return json.load(f)


def compute_summary(data):
    datasets = ["LIDC-IDRI", "BraTS", "CheXpert", "MSD"]
    categories = ["Structure", "Imaging", "Annotation", "Provenance", "Quality", "ML Readiness"]
    category_max = {"Structure": 6, "Imaging": 3, "Annotation": 4, "Provenance": 5, "Quality": 2, "ML Readiness": 2}

    summary = {}
    for cat in categories:
        dims = [d for d in data["dimensions"] if d["category"] == cat]
        summary[cat] = {
            "max": category_max[cat],
            "scores": {}
        }
        for ds in datasets:
            summary[cat]["scores"][ds] = sum(d[ds] for d in dims)

    totals = {}
    for ds in datasets:
        totals[ds] = sum(summary[cat]["scores"][ds] for cat in categories)

    percentages = {ds: totals[ds] / 22 * 100 for ds in datasets}
    average_pct = sum(percentages.values()) / len(percentages)
    gap_pct = 100 - average_pct

    category_averages = {}
    for cat in categories:
        avg = sum(summary[cat]["scores"][ds] for ds in datasets) / (len(datasets) * category_max[cat]) * 100
        category_averages[cat] = round(avg)

    return {
        "datasets": datasets,
        "categories": categories,
        "category_max": category_max,
        "summary": summary,
        "totals": totals,
        "percentages": percentages,
        "average_compliance": round(average_pct),
        "average_gap": round(gap_pct),
        "category_averages": category_averages
    }


def print_table(result):
    datasets = result["datasets"]
    categories = result["categories"]
    summary = result["summary"]

    print()
    print("Table 4: Compliance analysis (reproduced from per-dimension scores)")
    print("=" * 72)
    header = f"{'Category':<20}" + "".join(f"{ds:>12}" for ds in datasets) + f"{'VIDS':>8}"
    print(header)
    print("-" * 72)

    for cat in categories:
        max_val = summary[cat]["max"]
        row = f"{cat + ' (' + str(max_val) + ')':<20}"
        for ds in datasets:
            score = summary[cat]["scores"][ds]
            row += f"{score:>12.1f}"
        row += f"{max_val:>8}"
        print(row)

    print("-" * 72)
    row = f"{'Total (22)':<20}"
    for ds in datasets:
        row += f"{result['totals'][ds]:>12.1f}"
    row += f"{'22':>8}"
    print(row)

    row = f"{'Percentage':<20}"
    for ds in datasets:
        row += f"{result['percentages'][ds]:>11.0f}%"
    row += f"{'100%':>8}"
    print(row)
    print("=" * 72)

    print()
    print("Per-category averages (Figure 3):")
    print("-" * 40)
    for cat in categories:
        bar = "#" * (result["category_averages"][cat] // 2)
        print(f"  {cat:<16} {result['category_averages'][cat]:>3}%  {bar}")

    print()
    print(f"Average compliance: {result['average_compliance']}%")
    print(f"Average gap:        {result['average_gap']}%")
    print()


def main():
    parser = argparse.ArgumentParser(description="Verify VIDS compliance analysis scores")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    data = load_scores()
    result = compute_summary(data)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_table(result)


if __name__ == "__main__":
    main()
