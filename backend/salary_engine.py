class SalaryEngine:

    def get_salary_projection(
        self,
        role
    ):

        projections = {

            "Data Analyst": {
                "entry": "6-10 LPA",
                "3_years": "12-18 LPA",
                "5_years": "20-30 LPA"
            },

            "Analytics Engineer": {
                "entry": "8-14 LPA",
                "3_years": "18-28 LPA",
                "5_years": "30-45 LPA"
            },

            "Data Engineer": {
                "entry": "8-15 LPA",
                "3_years": "20-30 LPA",
                "5_years": "35-50 LPA"
            },

            "SDE": {
                "entry": "8-20 LPA",
                "3_years": "20-40 LPA",
                "5_years": "40-70 LPA"
            }

        }

        return projections.get(
            role,
            "Role Not Found"
        )