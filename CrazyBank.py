
class CrazyAccount:
    bank_title = "Crazy Bank"

    def __init__(self, customer_name, current_balance, minimum_balance, routing_number, account_number):



        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number
        self.__routing_number = routing_number

    def get_routing(self):
        return self.__routing_number

    def deposit(self, amount):
        self.current_balance += amount
        print("\nDeposit Successful.")
        print("Current Balance: \t{}\n".format(self.current_balance))

    def withdraw(self, amount):
        print("\nWithdrawal Requested.")
        if amount > self.current_balance:
            print("\nWithdrawal of {} failed. Current balance is below the minimum balance requirement.".format(amount))
            print("Current Balance: {}".format(self.current_balance))
            print("Minimum Balance: {}\n".format(self.minimum_balance))

        elif self.current_balance - amount < self.minimum_balance:
            print("\nWithdrawal of {} failed. Requested amount will put current balance below the minimum balance Required.".format(amount))
            print("Current Balance: {}".format(self.current_balance))
            print("Minimum Balance: {}\n".format(self.minimum_balance))

        else:
            self.current_balance -= amount
            print("\nWithdrawal of {} Successful.".format(amount))
            print("Current Balance: \t{}\n".format(self.current_balance))

    def print_customer_information(self):
        print("\n",CrazyAccount.bank_title)
        print("Customer Information-")
        print("Name: \t\t\t\t{}".format(self.customer_name))
        print("Current Balance: \t{}".format(self.current_balance))
        print("Minimum Balance: \t{}".format(self.minimum_balance))
        return 0
