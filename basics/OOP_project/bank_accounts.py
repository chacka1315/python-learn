class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, init_amount, acc_name):
        self._balance = init_amount
        self.name = acc_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self._balance:.2f}.")

    def get_balance(self):
        print(f"\n'{self.name}' balance is ${self._balance:.2f}.")

    def deposit(self, amount):
        # if type(amount) is not float or int:
        #     print("Provide valide amount.")
        # else:
        self._balance += amount
        print(f"\n✅ Success deposit on '{self.name}' account.")
        self.get_balance()

    def possible_transaction(self, amount):
        if self._balance >= amount:
            return
        else:
            raise BalanceException("\n❌ You don't have enough money.")

    def withdraw(self, amount):
        try:
            self.possible_transaction(amount)
            self._balance -= amount
            print(f"\n✅ Success withdraw.")
            self.get_balance()
        except Exception as error:
            print(error)

    def transfert(self, amount, account):
        try:
            self.possible_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print(f"\n✅ Success transfert.")
        except BalanceException as error:
            print(error)


class InterestsRewardsAcct(BankAccount):
    def deposit(self, amount):
        self._balance += amount * 1.05
        print(f"\n✅ Success interests deposit.")
        self.get_balance()


class SavingsAcct(InterestsRewardsAcct):
    def __init__(self, init_amount, acc_name):
        super().__init__(init_amount, acc_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.possible_transaction(amount + self.fee)
            self._balance -= self._balance + self.fee
            print(f"\n✅ Success withdraw.")
        except BalanceException as error:
            print(error)
