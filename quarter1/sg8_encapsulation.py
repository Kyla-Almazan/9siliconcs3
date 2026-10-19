class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number 
        self.__balance = 0.0
        self.set_balance(balance)
    def set_account_number(self, account_number):
        self.__account_number = account_number
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("The balance must not be a negative number.")
    @property
    def get_account_number(self):
        return self.__account_number
    @property
    def get_balance(self):
        return self.__balance

a = BankAccount(12345, 1000.0)
print(f"\nAccount 1")
print(f"Account Number: {a.get_account_number}")
print(f"Balance: {a.get_balance:.2f}")
print(f"\nUpdate balance to -100")
a.set_balance(-100)
print(f"Account Number: {a.get_account_number}")
print(f"Balance: {a.get_balance:.2f}")
