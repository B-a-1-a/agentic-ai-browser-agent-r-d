"""Count complaint and praise themes in store-reviews.csv.

Run from the study directory:  python3 data/theme_counts.py
Keyword matching is rough. Treat the output as a direction, not a measurement.
"""
import collections
import csv
import re
from pathlib import Path

ROWS = list(csv.DictReader(open(Path(__file__).with_name("store-reviews.csv"))))
ROWS = [r for r in ROWS if r["date"] >= "2025-10-01"]

THEMES = {
    "connection/setup breaks": r"\b(connect|disconnect|can'?t reach|not connect|pair|install the app|won'?t load|doesn'?t work|not working|broken|bug)",
    "cost/credits/limits": r"\b(credit|token|limit|usage|expensive|price|pricing|charg|refund|subscription|paid|pay)",
    "lost work/history/log": r"\b(history|lost|log\b|logs|session|resum|disappear|deleted|gone)",
    "permission/approval/babysit": r"\b(permission|approve|approval|allow once|babysit|confirm)",
    "security/trust/scary": r"\b(secur|scary|privacy|trust|bank|password|inject|dangerous|risk)",
    "parallel/background/isolation": r"\b(parallel|background|multiple tabs|several|isolat|at once|simultaneous|while i work|dedicated)",
    "slow": r"\b(slow|takes forever|sluggish|speed)",
    "too complex/needs coding": r"\b(complicated|confusing|coding|programming|developer|technical|learning curve|intuitive)",
}


def count(rows):
    return {
        name: sum(1 for r in rows if re.search(pattern, (r["title"] + " " + r["text"]).lower()))
        for name, pattern in THEMES.items()
    }


def main():
    negative = [r for r in ROWS if int(r["rating"]) <= 3]
    positive = [r for r in ROWS if int(r["rating"]) >= 4]
    neg_counts, pos_counts = count(negative), count(positive)
    print(f"1-3 star reviews: {len(negative)}   4-5 star reviews: {len(positive)}")
    for name in THEMES:
        print(
            f"{name:32s} 1-3★ {neg_counts[name]:4d} ({neg_counts[name] / len(negative):.0%})"
            f"   4-5★ {pos_counts[name]:4d} ({pos_counts[name] / len(positive):.0%})"
        )
    print()
    for product, n in collections.Counter(r["product"] for r in ROWS).most_common():
        ratings = [int(r["rating"]) for r in ROWS if r["product"] == product]
        print(f"{product:32s} n={n:4d}  avg={sum(ratings) / len(ratings):.2f}")


if __name__ == "__main__":
    main()
