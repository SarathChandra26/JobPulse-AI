import pandas as pd
import sqlite3

DB_PATH = "database/career_intelligence.db"

LINKEDIN_PATH = "data/raw/linkedin_jobs/linkedin_job_postings.csv"

SURVEY_PATH = "data/raw/stack_overflow/survey_results_public.csv"

conn = sqlite3.connect(DB_PATH)

print("Connected Successfully")

linkedin = pd.read_csv(
    LINKEDIN_PATH,
    low_memory=False
)

print("LinkedIn Dataset Loaded")
print(linkedin.shape)

linkedin = linkedin[
    [
        "job_title",
        "company",
        "job_location",
        "search_city",
        "search_country",
        "job_level",
        "job_type",
        "first_seen"
    ]
]
print(linkedin.head())
linkedin = linkedin.dropna(
    subset=["job_title"]
)

linkedin["company"] = linkedin[
    "company"
].fillna("Unknown")

linkedin["job_location"] = linkedin[
    "job_location"
].fillna("Unknown")
linkedin.to_sql(
    "linkedin_jobs",
    conn,
    if_exists="replace",
    index=False
)

print("LinkedIn Loaded Into SQLite")
survey = pd.read_csv(
    SURVEY_PATH,
    low_memory=False
)

print("Survey Loaded")
print(survey.shape)
survey = survey[
    [
        "ResponseId",
        "Country",
        "Employment",
        "DevType",
        "YearsCode",
        "CompTotal",
        "ConvertedCompYearly",
        "LanguageHaveWorkedWith",
        "DatabaseHaveWorkedWith",
        "PlatformHaveWorkedWith",
        "AIModelsHaveWorkedWith",
        "AIThreat",
        "AIHuman",
        "AIAcc"
    ]
]
survey["ConvertedCompYearly"] = pd.to_numeric(
    survey["ConvertedCompYearly"],
    errors="coerce"
)

survey = survey[
    survey["ConvertedCompYearly"].notna()
]
survey.to_sql(
    "developer_survey",
    conn,
    if_exists="replace",
    index=False
)

print("Survey Loaded Into SQLite")
conn.close()

print("ETL Completed Successfully")