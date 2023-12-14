from pythonProject.python_oop.exams.final_exam.project.clients.base_client import BaseClient


class Adult(BaseClient):
    __INTEREST = 4.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, Adult.__INTEREST)

    def increase_clients_interest(self):
        self.interest += 2
