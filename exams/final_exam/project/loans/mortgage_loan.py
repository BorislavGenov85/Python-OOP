from pythonProject.python_oop.exams.final_exam.project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    __INTEREST_RATE = 3.5
    __AMOUNT = 50000.0

    def __init__(self):
        super().__init__(MortgageLoan.__INTEREST_RATE, MortgageLoan.__AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += 0.5
