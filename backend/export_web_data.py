import pandas as pd
from pathlib import Path

PROCESSED = Path("data/processed")
FRONTEND = Path("frontend/data")

FRONTEND.mkdir(
    parents=True,
    exist_ok=True
)

files = [
    "top_jobs.csv",
    "top_companies.csv",
    "top_countries.csv",
    "salary_roles.csv"
]

for file in files:

    df = pd.read_csv(
        PROCESSED / file
    )

    json_name = file.replace(
        ".csv",
        ".json"
    )

    df.to_json(
        FRONTEND / json_name,
        orient="records",
        indent=4
    )

    print(
        f"{json_name} exported"
    )

print("All JSON exports complete")