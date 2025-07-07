from CrazyBank import CrazyAccount

class SavingsAccount(CrazyAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, routing_number, account_number):
        super(SavingsAccount, self).__init__(customer_name, current_balance, minimum_balance, routing_number, account_number)
        self.interest_rate = 0.05


    def monthly_interest(self):
        interest = self.current_balance * self.interest_rate
        self.current_balance += interest
        print(f"\nInterest Rate of ${interest:.2f} applied.")
        print(f"Current Balance: \t{self.current_balance:.2f}\n")
