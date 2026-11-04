"""Exercise 02: CSV match summary."""

import csv
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "match_summary.csv"
rows = [{"bot": "student", "wins": 2}, {"bot": "wait", "wins": 0}]

path.parent.mkdir(parents=True, exist_ok=True)
with path.open("w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["bot", "wins"])
    writer.writeheader()
    writer.writerows(rows)

with path.open("r", encoding="utf-8", newline="") as file:
    loaded_rows = list(csv.DictReader(file))

for row in loaded_rows:
    row["wins"] = int(row["wins"])
    print(row)
