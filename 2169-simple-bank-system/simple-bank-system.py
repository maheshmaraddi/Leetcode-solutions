
class Bank:
    def __init__(self, balance: List[int]):
        self.bal = balance
        print(self.bal)

    def is_valid_account(self, account: int) -> bool:
        return 1 <= account <= len(self.bal)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.is_valid_account(account1) and self.is_valid_account(account2):
            if self.bal[account1-1] >= money:
                self.bal[account1-1] -= money
                self.bal[account2-1] += money
                return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.is_valid_account(account):
            self.bal[account-1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.is_valid_account(account):
            if self.bal[account-1] >= money:
                self.bal[account-1] -= money
                return True
        return False