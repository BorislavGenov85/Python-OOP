from pythonProject.python_oop.exams.final_exam.project.clients.adult import Adult
from pythonProject.python_oop.exams.final_exam.project.clients.student import Student
from pythonProject.python_oop.exams.final_exam.project.loans.mortgage_loan import MortgageLoan
from pythonProject.python_oop.exams.final_exam.project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENT_TYPES = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans = []
        self.clients = []

    def add_loan(self, loan_type: str):
        if loan_type not in BankApp.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        loan = BankApp.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in BankApp.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        client = BankApp.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = next(filter(lambda c: c.client_id == client_id, self.clients))
        loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans))

        if isinstance(client, Student) and not isinstance(loan, StudentLoan):
            raise Exception("Inappropriate loan type!")

        if isinstance(client, Adult) and not isinstance(loan, MortgageLoan):
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except StopIteration:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        count = 0
        for loan in self.loans:
            if isinstance(loan, StudentLoan) and loan_type == 'StudentLoan':
                loan.increase_interest_rate()
                count += 1
            elif isinstance(loan, MortgageLoan) and loan_type == "MortgageLoan":
                loan.increase_interest_rate()
                count += 1

        return f"Successfully changed {count} loans."

    def increase_clients_interest(self, min_rate: float):
        count = 0
        for client in self.clients:
            if isinstance(client, Student) and client.interest < min_rate:
                client.increase_clients_interest()
                count += 1
            elif isinstance(client, Adult) and client.interest < min_rate:
                client.increase_clients_interest()
                count += 1

        return f"Number of clients affected: {count}."

    def get_statistics(self):
        total = 0
        for client in self.clients:
            for loan in client.loans:
                if isinstance(loan, (StudentLoan, MortgageLoan)):
                    total += loan.amount

        total_sum = 0
        for loan in self.loans:
            if isinstance(loan, (StudentLoan, MortgageLoan)):
                total_sum += loan.amount

        average_rate = 0
        if self.clients:
            average_rate += sum([c.interest for c in self.clients]) / len(self.clients)

        result = f"Active Clients: {len(self.clients)}\nTotal Income: {sum(c.income for c in self.clients):.2f}\n" \
                 f"Granted Loans: {sum(len(c.loans) for c in self.clients)}, " \
                 f"Total Sum: {total:.2f}\n" \
                 f"Available Loans: {len(self.loans)}, " \
                 f"Total Sum: {sum(loan.amount for loan in self.loans):.2f}\n" \
                 f"Average Client Interest Rate: {average_rate:.2f}"

        return result
