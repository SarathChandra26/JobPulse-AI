class RoadmapEngine:

    def get_roadmap(self, role):

        roadmaps = {

            "Data Analyst": [

                "Learn SQL",

                "Learn Python",

                "Learn Pandas",

                "Learn Statistics",

                "Learn Power BI",

                "Build JobPulse AI",

                "Prepare for Interviews"
            ],

            "Analytics Engineer": [

                "Advanced SQL",

                "Python",

                "ETL Pipelines",

                "Data Modeling",

                "dbt Fundamentals",

                "Cloud Basics",

                "Build Analytics Projects"
            ],

            "Data Engineer": [

                "SQL",

                "Python",

                "ETL",

                "Spark",

                "Data Warehousing",

                "Cloud",

                "Pipeline Projects"
            ],

            "SDE": [

                "Java",

                "DSA",

                "OOP",

                "DBMS",

                "Operating Systems",

                "System Design",

                "Full Stack Project"
            ]
        }

        return roadmaps.get(
            role,
            ["Roadmap Not Found"]
        )