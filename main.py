from CrazySavings import *
from CrazyChecking import *

def main():

    checking_acc1 = CheckingAccount("Walter White", 10000, 500, 10000001, 1000002)
    checking_acc2 = CheckingAccount("Bruno Mars", 1000, 500, 10000003, 1000004)
    savings_acc1 = SavingsAccount("Bang Chan", 10000, 500, 10000005, 1000006)
    savings_acc2 = SavingsAccount("Oliver Tree", 10000, 500, 10000007, 1000008)


    """SCENARIO #1: Walter white deposits $1000, then he tries to 
    withdraw $1000 back. But the limit of withdrawal on a cheking 
    account is $500, so he gets a message for withdrawal failure"""

    checking_acc1.deposit(1000)
    checking_acc1.withdraw(1000)

    # END SCENARIO #1

    """SCENARIO #2: Bruno Mars withdraws $500 from his $1000 balance, 
    then he tries to withdraw the rest of the $500. This fails as he 
    is trying to withdraw more than minimum balance."""

    checking_acc2.withdraw(500)
    checking_acc2.withdraw(500)

    # END SCENARIO #2

    """SCENARIO #3: Bang Chan deposits 1000 and his monthly interest 
    rate is applied."""

    savings_acc1.withdraw(1000)
    savings_acc2.monthly_interest()

    # END SCENARIO #3

    """SCENARIO #4: Oliver Tree has had his account open for two months
    so his interest rate has been applied twice since his account opened."""

    savings_acc2.monthly_interest()
    savings_acc2.monthly_interest()

    # END SCENARIO #4

if __name__ == "__main__":
    main()