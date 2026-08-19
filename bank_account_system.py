class BankAccount:
    bank_name = "National Bank"
    total_account = 0

    def __init__(self, owner_name, balance, account_no):
        self.owner_name = owner_name
        self.balance = balance
        self.account_no = account_no
        self.transaction_count = 0
        BankAccount.total_account += 1

    def deposit(self, amount):
        if amount <= 0:
            print("please enter valid amount")
            return
        self.balance += amount
        self.transaction_count += 1
        print(f"You Deposit Amount is {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            print("enter valid amount")
            return
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_count += 1
            print(f"Please Collect your money {amount}")
        else:
            print("Insufficinet Balance")

    def __add__(self, other):
        if isinstance(other, BankAccount):
            new_name = f"{self.owner_name} & {other.owner_name}"
            combine_balance = self.balance + other.balance
            new_acc_no = f"{self.account_no}-{other.account_no}"
            return BankAccount(new_name, combine_balance, new_acc_no)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.account_no == other.account_no
        return False

    def info(self):
        print(f"Thanks for creating your account in {self.bank_name}")
        print(f"Account Owner Name {self.owner_name} |Account No {self.account_no}| Balance {self.balance} | Total transaction: {self.transaction_count}")

    @classmethod
    def get_total_account(cls):
        print(f"Total Bank Accounts are {cls.total_account}")


 
account1 = BankAccount("Mudasir Manzoor", 1000, 1234)
account2 = BankAccount("Ali Khan", 2000, 1237)

account1.info()
account2.info()


account1.deposit(1500)
account2.deposit(2000)

account1.withdraw(1200)
account2.withdraw(1000)

combined_account = account1 + account2 
combined_account.info()

BankAccount.get_total_account()
