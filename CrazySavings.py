from CrazyBank import CrazyAccount

class BankAccount(CrazyAccount):

    def __init__(self):
        super(BankAccount, self).__init__()
        self.interest_rate = 0.05


    def monthly_interest(self, current_balance):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print("Interest Rate of ${} applied.".format(interest))
        print("Current Balance: \t{}".format(self.current_balance))