class BankAccount:
    class Transaction:
        def __init__(self, transaction_id, transaction_type, amount, date):
            self.transaction_id = transaction_id
            self.transaction_type = transaction_type
            self.amount = amount
            self.date = date

        def __str__(self):
            return f"Transaction ID: {self.transaction_id}, Type: {self.transaction_type}, Amount: ${self.amount}, Date: {self.date}"

    def __init__(self, account_holder, account_number, balance, account_type):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type
        self.transactions = []

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Account Type: {self.account_type}, Balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        transaction = self.Transaction(len(self.transactions) + 1, "Deposit", amount, "2025-02-08")
        self.transactions.append(transaction)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            transaction = self.Transaction(len(self.transactions) + 1, "Withdrawal", amount, "2025-02-08")
            self.transactions.append(transaction)
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.balance

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

account1 = BankAccount("Alice Smith", "123456789", 5000.00, "Checking")
print(account1)

account1.deposit(2000.00)

account1.withdraw(1000.00)

print("Current Balance:", account1.get_balance())

account1.account_type = "Savings"
print(account1)

del account1.account_number
print(account1)

print("\nTransactions:")
for transaction in account1.transactions:
    print(transaction)

del account1
