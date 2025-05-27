class Account:
 def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
        self.loan_history = []

 def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.deposits.append
            print(f"You have deposited {amount}, your new balance {self.balance}")
        else:
            print("Invalid deposit amount.")


 def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.withdrawals.append
            print(f"Withdrawn: {amount}, New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

 def show_balance(self):
        print(f"Current balance: {self.balance}")

 def transfer(self, amount, recipient):
        if 0 < amount <= self.balance:
            self.balance -= amount
            recipient.deposit(amount)
            print(f"Transferred: {amount} to {recipient.name}")
        else:
            print("Insufficient funds or invalid amount for transfer.")

 def loan(self, amount):
      if self.loan_balance == 0:
        self.loan_balance = amount
        self.balance += amount
        self.loan_history.append(f"Loan taken: {amount}, Outstanding loan: {self.loan_balance}")
        print(f"Loan taken: {amount}, Outstanding loan: {self.loan_balance}, Current balance: {self.balance}")
      else:
        print("Outstanding loan exists. Repay it first.")

 def repay_loan(self, amount):
        if amount <= self.loan_balance and amount > 0 :
          self.loan_balance -= amount
          self.balance -= amount
          self.loan_history.append(f"Loan repaid: {amount}, Remaining loan: {self.loan_balance}")
          print(f"Loan repaid: {amount}, Remaining loan: {self.loan_balance}, Current balance: {self.balance}")
        elif amount > self.loan_balance:
            print(f"Amount exceeds outstanding loan. Remaining loan {self.loan_balance}")
        else:
          print("Invalid amount.")

 def get_statement(self):
        print("Statement:")
        for transaction in self.deposits + self.withdrawals:
            print(transaction)

 def get_loan_statement(self):
      print("Loan Statement:")
      for record in self.loan_history:
        print(record)
def interest_calculation(self):
        interest=self.balance * 0.05
        self.balance +=interest
        self.interest.append(interest)
        self.statements.append(f"Hello {self.name},You have applies an interest of {interest}, your new balance is {self.balance}.")
        return f"Hello {self.name},You have applies an interest of {interest}, your new balance is {self.balance}."
def freeze_account(self):
        self.is_frozen=True
        self.statements.append(f"Hello {self.name}, your account has been frozen")
        return f"Hello {self.name}, your account has been frozen"
def unfreeze_account(self):
        self.is_frozen=False
        self.statements.append(f"Hello {self.name}, your account has been unfrozen.")
        return f"Hello {self.name}, your account has been unfrozen."
def set_minimum_balance(self,amount):
        self.minimum_balance=amount
        self.statements.append(f"Hello {self.name}, your minimum balance is set to {self.minimum_balance}.")
        return f"Hello {self.name}, your minimum balance is set to {self.minimum_balance}."
def close_account(self):
        self.balance=0
        self.loan=0
        self.deposites.clear()
        self.withdrawals.clear()
        self.request_loans.clear()
        self.interest.clear()
        self.statements.append(f"Hello {self.name}, your transactions are cleared.")
        return f"Hello {self.name}, your transactions are cleared."
def account_statement(self):
        for statement in self.statements:
            return self.statements