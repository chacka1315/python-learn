from bank_accounts import *

elon = BankAccount(300_000, "Elon")
siaka = BankAccount(400_000, "Siaka")

# siaka.deposit(1_450_060)
# elon.withdraw(150_000)

elon.transfert(90_000, siaka)

elon.get_balance()
siaka.get_balance()

felix = InterestsRewardsAcct(200_000, "Felix")
felix.deposit(100_000)

naval = SavingsAcct(800_000, "Naval")
naval.deposit(599)

naval.transfert(105_000, siaka)
