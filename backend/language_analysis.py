import sqlite3
import pandas as pd

conn = sqlite3.connect(
    "database/career_intelligence.db"
)

df = pd.read_sql(
    """
    SELECT LanguageHaveWorkedWith
    FROM developer_survey
    WHERE LanguageHaveWorkedWith IS NOT NULL
    """,
    conn
)

languages = {}

for row in df[
    "LanguageHaveWorkedWith"
]:
    for language in str(row).split(";"):
        languages[language] = (
            languages.get(language, 0) + 1
        )

result = (
    pd.DataFrame(
        languages.items(),
        columns=[
            "language",
            "count"
        ]
    )
    .sort_values(
        "count",
        ascending=False
    )
)

print(result.head(20))