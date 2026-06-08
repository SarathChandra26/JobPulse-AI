import pandas as pd
from analytics import AnalyticsEngine
from pathlib import Path


OUTPUT_DIR = Path("data/processed")

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

engine = AnalyticsEngine()

print("Export Started...")

# ---------------------------------
# Jobs
# ---------------------------------

jobs = engine.top_job_titles()

jobs.to_csv(
    OUTPUT_DIR / "top_jobs.csv",
    index=False
)

print("top_jobs.csv exported")

# ---------------------------------
# Companies
# ---------------------------------

companies = engine.top_companies()

companies.to_csv(
    OUTPUT_DIR / "top_companies.csv",
    index=False
)

print("top_companies.csv exported")

# ---------------------------------
# Countries
# ---------------------------------

countries = engine.top_countries()

countries.to_csv(
    OUTPUT_DIR / "top_countries.csv",
    index=False
)

print("top_countries.csv exported")

# ---------------------------------
# Salary
# ---------------------------------

salary = engine.highest_paying_roles()

salary.to_csv(
    OUTPUT_DIR / "salary_roles.csv",
    index=False
)

print("salary_roles.csv exported")

print("Export Completed Successfully")

engine = AnalyticsEngine()

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "frontend" / "data"

DATA_DIR.mkdir(exist_ok=True)
engine.total_companies().to_json(
    DATA_DIR / "total_companies.json",
    orient="records"
)

engine.total_countries().to_json(
    DATA_DIR / "total_countries.json",
    orient="records"
)

engine.average_salary().to_json(
    DATA_DIR / "average_salary.json",
    orient="records"
)
