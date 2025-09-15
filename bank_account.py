class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance
        self.overdraft_limit = 0

    def set_overdraft_limit(self, limit):
        if limit < 0:
            raise ValueError("Overdraft limit cannot be negative.")
        self.overdraft_limit = limit

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Cannot withdraw more than the current balance and overdraft limit.")
        self.balance -= amount

    def get_overdraft_limit(self):
        return self.overdraft_limit
    
    def get_account_info(self):
        return {"balance": self.balance, "overdraft_limit": self.overdraft_limit}

    def get_balance(self):
        return self.balance