class CareerAdvisor:

    def __init__(self):

        self.roles = {

            "Data Analyst": {

                "skills": [
                    "SQL",
                    "Python",
                    "Excel",
                    "Power BI",
                    "Statistics"
                ],

                "certifications": [
                    "SQL and Relational Databases 101",
                    "Data Analysis with Python",
                    "Microsoft Power BI"
                ],

                "projects": [
                    "JobPulse AI",
                    "Customer Churn Analysis",
                    "Sales Analytics Dashboard"
                ],

                "salary": "6-10 LPA",

                "demand": "High"
            },

            "Analytics Engineer": {

                "skills": [
                    "SQL",
                    "Python",
                    "ETL",
                    "Data Modeling",
                    "Analytics Engineering"
                ],

                "certifications": [
                    "dbt Fundamentals",
                    "Data Engineering Basics",
                    "SQL Advanced"
                ],

                "projects": [
                    "JobPulse AI",
                    "Modern Data Warehouse",
                    "Analytics Pipeline"
                ],

                "salary": "8-14 LPA",

                "demand": "Very High"
            },

            "Data Engineer": {

                "skills": [
                    "SQL",
                    "Python",
                    "Spark",
                    "ETL",
                    "Data Warehousing"
                ],

                "certifications": [
                    "Data Engineering",
                    "Spark Basics",
                    "Cloud Fundamentals"
                ],

                "projects": [
                    "Data Lake Project",
                    "ETL Pipeline",
                    "JobPulse AI"
                ],

                "salary": "8-15 LPA",

                "demand": "Very High"
            },

            "Business Analyst": {

                "skills": [
                    "Excel",
                    "SQL",
                    "Power BI",
                    "Business Analysis",
                    "Stakeholder Management"
                ],

                "certifications": [
                    "Business Analysis Fundamentals"
                ],

                "projects": [
                    "Market Analysis",
                    "Customer Analytics"
                ],

                "salary": "6-12 LPA",

                "demand": "High"
            },

            "Product Analyst": {

                "skills": [
                    "SQL",
                    "Python",
                    "A/B Testing",
                    "Product Metrics",
                    "Analytics"
                ],

                "certifications": [
                    "Product Analytics"
                ],

                "projects": [
                    "Product Analytics Dashboard",
                    "User Behavior Analysis"
                ],

                "salary": "10-18 LPA",

                "demand": "High"
            },

            "SDE": {

                "skills": [
                    "Java",
                    "DSA",
                    "OOP",
                    "DBMS",
                    "System Design"
                ],

                "certifications": [
                    "Oracle Java"
                ],

                "projects": [
                    "Full Stack Project",
                    "JobPulse AI"
                ],

                "salary": "8-20 LPA",

                "demand": "Very High"
            }

        }

    def get_role_info(self, role):

        return self.roles.get(
            role,
            "Role Not Found"
        )