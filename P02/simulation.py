from youthaccount import YouthAccount
from savingaccount import SavingAccount
from datetime import *

def wait_youth_account(youth_account, months):
    for month in range(0, months):
        youth_account.pay_interest()

def wait_savings_account(saving_account, months):
    for month in range(0, months):
        saving_account.pay_interest()
        saving_account.reset_withdraw_limit()

def main():
    print('Youth account test:')
    youth_test_account = YouthAccount(12, 'CH1313')
    youth_test_account.deposit(10000)
    wait_youth_account(youth_account=youth_test_account, months=3)
    youth_test_account.print_balance()
    youth_test_account.withdraw(2000)
    youth_test_account.print_balance()
    youth_test_account.withdraw(20000)
    youth_test_account.print_balance()
    print('-----------------------------')

    print('Savings account test:')
    saving_test_account = SavingAccount(12, 'CH1313')
    saving_test_account.deposit(10000)
    wait_savings_account(saving_account=saving_test_account, months=3)
    saving_test_account.print_balance()
    saving_test_account.withdraw(1000)
    saving_test_account.print_balance()
    saving_test_account.withdraw(20000)
    saving_test_account.print_balance()
    
    
if __name__ == "__main__":
    main()