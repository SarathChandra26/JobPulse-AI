import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "career_intelligence.db"


class AnalyticsEngine:

    def get_connection(self):
        return sqlite3.connect(DB_PATH)

    def total_jobs(self):

        query = """
        SELECT COUNT(*) AS total_jobs
        FROM linkedin_jobs
        """

        with self.get_connection() as conn:
            return pd.read_sql(query, conn)

    def top_job_titles(self):

        query = """
        SELECT
            job_title,
            COUNT(*) AS total_jobs
        FROM linkedin_jobs
        GROUP BY job_title
        ORDER BY total_jobs DESC
        LIMIT 20
        """

        with self.get_connection() as conn:
            return pd.read_sql(query, conn)

    def top_companies(self):

        query = """
        SELECT
            company,
            COUNT(*) AS total_jobs
        FROM linkedin_jobs
        GROUP BY company
        ORDER BY total_jobs DESC
        LIMIT 20
        """

        with self.get_connection() as conn:
            return pd.read_sql(query, conn)

    def top_countries(self):

        query = """
        SELECT
            search_country,
            COUNT(*) AS total_jobs
        FROM linkedin_jobs
        GROUP BY search_country
        ORDER BY total_jobs DESC
        """

        with self.get_connection() as conn:
            return pd.read_sql(query, conn)

    def highest_paying_roles(self):

        query = """
        SELECT
            DevType,
            AVG(ConvertedCompYearly) AS avg_salary
        FROM developer_survey
        WHERE DevType IS NOT NULL
        GROUP BY DevType
        ORDER BY avg_salary DESC
        LIMIT 20
        """

        with self.get_connection() as conn:
            return pd.read_sql(query, conn)

    def total_companies(self):

        query = """
        SELECT COUNT(DISTINCT company)
        AS total_companies
        FROM linkedin_jobs
        """

        with self.get_connection() as conn:
            return pd.read_sql(query, conn)

    def total_countries(self):

        query = """
        SELECT COUNT(DISTINCT search_country)
        AS total_countries
        FROM linkedin_jobs
        """

        with self.get_connection() as conn:
            return pd.read_sql(query, conn)

    def average_salary(self):

        query = """
        SELECT ROUND(
            AVG(ConvertedCompYearly),
            0
        ) AS avg_salary
        FROM developer_survey
        WHERE ConvertedCompYearly IS NOT NULL
        """

        with self.get_connection() as conn:
            return pd.read_sql(query, conn)