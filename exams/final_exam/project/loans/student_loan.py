from pythonProject.python_oop.exams.final_exam.project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    __INTEREST_RATE = 1.5
    __AMOUNT = 2000.0

    def __init__(self):
        super().__init__(StudentLoan.__INTEREST_RATE, StudentLoan.__AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.2
