class Bank:
    def __init__(self):
        self.users = []
        self.total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_account(self, name, initial_balance):
        user = User(name, initial_balance)
        self.users.append(user)
        self.total_balance += initial_balance

    def get_total_balance(self):
        return self.total_balance

    def get_total_loan_amount(self):
        return self.total_loan_amount

    def enable_loan_feature(self):
        self.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.loan_feature_enabled = False


class User:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.loan_limit = initial_balance * 2
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: {amount}")

    def withdraw(self, amount, bank):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: {amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount, bank):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transfer: {amount} to {recipient.name}")
            recipient.transaction_history.append(f"Transfer: {amount} from {self.name}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        return self.balance

    def take_loan(self, bank):
        if bank.loan_feature_enabled:
            loan_amount = self.balance * 2
            self.balance += loan_amount
            self.total_loan_amount += loan_amount
            self.transaction_history.append(f"Loan taken: {loan_amount}")
        else:
            print("Bank's loan feature is currently disabled!")


class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, initial_balance):
        self.bank.create_account(name, initial_balance)

    def check_total_balance(self):
        return self.bank.get_total_balance()

    def check_total_loan_amount(self):
        return self.bank.get_total_loan_amount()

    def enable_loan_feature(self):
        self.bank.enable_loan_feature()

    def disable_loan_feature(self):
        self.bank.disable_loan_feature()


# Example usage
bank = Bank()
admin = Admin(bank)

admin.create_account("Amin", 1000)
admin.create_account("Bobi", 500)

amin = bank.users[0]
bobi = bank.users[1]

amin.deposit(200)
bobi.deposit(100)

amin.withdraw(100, bank)
bobi.transfer(amin, 50, bank)

print(amin.check_balance())  # Output: 1100
print(bobi.check_balance())    # Output: 550

amin.take_loan(bank)
print(amin.check_balance())  # Output: 3400
print(bank.get_total_loan_amount())  # Output: 3000

admin.disable_loan_feature()
amin.take_loan(bank)  # Output: Bank's loan feature is currently disabled!

print(admin.check_total_balance())  # Output: 4100
print(admin.check_total_loan_amount())  # Output: 3000
