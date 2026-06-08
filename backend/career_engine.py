from backend.recommendation_engine import CareerAdvisor
from backend.salary_engine import SalaryEngine
from backend.roadmap_engine import RoadmapEngine


class CareerEngine:

    def __init__(self):

        self.advisor = CareerAdvisor()

        self.salary = SalaryEngine()

        self.roadmap = RoadmapEngine()

    def get_complete_profile(
        self,
        role
    ):

        return {

            "role_info":
                self.advisor.get_role_info(role),

            "salary":
                self.salary.get_salary_projection(role),

            "roadmap":
                self.roadmap.get_roadmap(role)
        }