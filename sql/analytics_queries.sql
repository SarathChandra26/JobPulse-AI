SELECT                              "Top Hiring Job Titles"
    job_title,
    COUNT(*) AS total_jobs
FROM linkedin_jobs
GROUP BY job_title
ORDER BY total_jobs DESC
LIMIT 20;

SELECT                              "Top Hiring Companies"
    company,
    COUNT(*) AS total_jobs
FROM linkedin_jobs
GROUP BY company
ORDER BY total_jobs DESC
LIMIT 20;

SELECT                              "Most Active Countries"
    search_country,
    COUNT(*) AS total_jobs
FROM linkedin_jobs
GROUP BY search_country
ORDER BY total_jobs DESC;

SELECT                              "Job Types"
    job_type,
    COUNT(*) AS total_jobs
FROM linkedin_jobs
GROUP BY job_type
ORDER BY total_jobs DESC;

SELECT                             "Highest Paying Developer Roles"
    DevType,
    ROUND(
        AVG(ConvertedCompYearly),
        2
    ) AS avg_salary
FROM developer_survey
WHERE DevType IS NOT NULL
GROUP BY DevType
ORDER BY avg_salary DESC
LIMIT 20;

SELECT                              "Highest Paying Countries"
    Country,
    ROUND(
        AVG(ConvertedCompYearly),
        2
    ) AS avg_salary
FROM developer_survey
GROUP BY Country
HAVING COUNT(*) > 50
ORDER BY avg_salary DESC
LIMIT 20;

SELECT                                "AI Adoption Trends"
    AIThreat,
    COUNT(*) AS total
FROM developer_survey
GROUP BY AIThreat;


