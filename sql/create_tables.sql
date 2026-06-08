DROP TABLE IF EXISTS linkedin_jobs;

CREATE TABLE linkedin_jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    company TEXT,
    job_location TEXT,
    search_city TEXT,
    search_country TEXT,
    job_level TEXT,
    job_type TEXT,
    first_seen TEXT
);

DROP TABLE IF EXISTS developer_survey;

CREATE TABLE developer_survey (
    ResponseId INTEGER PRIMARY KEY,

    Country TEXT,
    Employment TEXT,
    DevType TEXT,

    YearsCode TEXT,

    CompTotal REAL,
    ConvertedCompYearly REAL,

    LanguageHaveWorkedWith TEXT,
    DatabaseHaveWorkedWith TEXT,
    PlatformHaveWorkedWith TEXT,

    AIModelsHaveWorkedWith TEXT,
    AIThreat TEXT,
    AIHuman TEXT,
    AIAcc TEXT
);