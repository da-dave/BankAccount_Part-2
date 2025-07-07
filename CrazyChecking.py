from CrazyBank import CrazyAccount


class CheckingAccount(CrazyAccount):

    def __init__(self, customer_name, current_balance, minimum_balance, routing_number, account_number):
        super(CheckingAccount, self).__init__(customer_name, current_balance, minimum_balance, routing_number, account_number)
        self.withdrawal_limit = 500


    #
    def withdraw(self, amount):
        print("\nWithdrawal Requested. Withdrawal limit is $500")

        if amount > self.withdrawal_limit:
            print("\nWithdrawal of {} failed. Requested amount exceeds withdraw limit.".format(amount))
            print("Current Balance: {}".format(self.current_balance))
            print("Minimum Balance: {}\n".format(self.minimum_balance))

        else:
            super().withdraw(amount)