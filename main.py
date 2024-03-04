"""BankAccount"""


class BankAccount:
    """Представлення банківського рахунку"""
    def __init__(self, count):
        self.count = count

    def withdraw(self, tr):
        """Зняття з рахунку"""
        if tr > self.count:
            print("Error")
        else:
            self.count -= tr

    def topup(self, tr):
        """Поповнення рахунку"""
        self.count += tr

    def __str__(self):
        return f"You account balance is: {self.count}"


account = BankAccount(100)
account.withdraw(50)
account.topup(200)
print(account)
