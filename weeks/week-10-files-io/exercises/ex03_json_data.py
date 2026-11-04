"""Exercise 03: JSON-compatible replay data."""

import json
from pathlib import Path

WEEK_ROOT = Path(__file__).resolve().parents[1]
path = WEEK_ROOT / ".learner-output" / "replay.json"
replay = {
    "format": "COURSE LOCAL FORMAT",
    "production_compatibility": "NOT VUACOC PRODUCTION FORMAT",
    "turns": [],
}

path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(replay, ensure_ascii=False, indent=2), encoding="utf-8")
loaded = json.loads(path.read_text(encoding="utf-8"))

assert loaded["format"] == "COURSE LOCAL FORMAT"
assert loaded["production_compatibility"] == "NOT VUACOC PRODUCTION FORMAT"
print(loaded["turns"])
