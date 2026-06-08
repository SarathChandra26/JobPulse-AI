import sqlite3

conn = sqlite3.connect(
    "database/career_intelligence.db"
)

cursor = conn.cursor()

with open(
    "sql/create_tables.sql",
    "r",
    encoding="utf-8"
) as f:

    cursor.executescript(
        f.read()
    )

conn.commit()

print("Tables created successfully")