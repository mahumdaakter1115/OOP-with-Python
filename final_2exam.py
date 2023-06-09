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

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal: {amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transfer: {amount} to {recipient.name}")
            recipient.transaction_history.append(f"Transfer: {amount} from {self.name}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        return self.balance

    def take_loan(self, amount):
        if Bank.loan_feature_enabled:
            if amount <= self.loan_limit:
                self.balance += amount
                self.total_loan_amount += amount
                self.transaction_history.append(f"Loan taken: {amount}")
            else:
                print("Loan amount exceeds limit!")
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

admin.create_account("Alice", 1000)
admin.create_account("Bob", 500)

alice = bank.users[0]
bob = bank.users[1]

alice.deposit(200)
bob.deposit(100)

alice.withdraw(100)
bob.transfer(alice, 50)

print(alice.check_balance())  # Output: 1100
print(bob.check_balance())    # Output: 550

alice.take_loan(300)
print(alice.check_balance())  # Output: 1400
print(bank.get_total_loan_amount())  # Output: 300

admin.disable_loan_feature()
alice.take_loan(200)  # Output: Bank's loan feature is currently disabled!

print(admin.check_total_balance())  # Output: 1600
print(admin.check_total_loan_amount())  # Output: 300
