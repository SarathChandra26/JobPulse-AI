import json
from pathlib import Path

from backend.career_engine import CareerEngine

engine = CareerEngine()

roles = [

    "Data Analyst",
    "Analytics Engineer",
    "Data Engineer",
    "Business Analyst",
    "Product Analyst",
    "SDE"
]

output = {}

for role in roles:

    output[role] = engine.get_complete_profile(
        role
    )

Path(
    "frontend/data"
).mkdir(
    parents=True,
    exist_ok=True
)

with open(
    "frontend/data/career_profiles.json",
    "w"
) as f:

    json.dump(
        output,
        f,
        indent=4
    )

print(
    "career_profiles.json exported"
)