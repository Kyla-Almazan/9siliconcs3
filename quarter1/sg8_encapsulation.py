class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number 
        self._balance = 0.0
        self.set_balance(balance)
    def set_account_number(self, account_number):
        self._account_number = account_number
    def set_balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            print("The balance must not be a negative number.")
    @property
    def account_number(self):
        return self._account_number
    @property
    def balance(self):
        return self._balance

a = BankAccount(12345, 1000.0)
print(f"\nAccount 1")
print(f"Account Number: {a.account_number}")
print(f"Balance: {a.balance:.2f}")
print(f"\nUpdate balance to -100")
a.set_balance(-100)
print(f"Account Number: {a.account_number}")
print(f"Balance: {a.balance:.2f}")