from backend.analytics import AnalyticsEngine

def get_dashboard_kpis():

    engine = AnalyticsEngine()

    total_jobs_df = engine.total_jobs()
    top_jobs_df = engine.top_job_titles()
    top_companies_df = engine.top_companies()
    top_countries_df = engine.top_countries()

    return {
        "total_jobs": int(total_jobs_df.iloc[0]["total_jobs"]),
        "top_job": str(top_jobs_df.iloc[0]["job_title"]),
        "top_company": str(top_companies_df.iloc[0]["company"]),
        "top_country": str(top_countries_df.iloc[0]["search_country"])
    }