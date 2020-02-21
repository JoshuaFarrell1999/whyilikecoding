pin_number = 7073
acc_balance = 256

def cash_withdrawal(amount,accnum):
    print("withdrawing {} from account {}".format(amount,accnum))
def security_check():
    pin_entered = int(input("Please enter your PIN number"))
    if pin_entered != pin_number:
        print("PIN number incorrect, please try again") 
        security_check()
    else:
        withdrawal_request()
def withdrawal_request():
    global acc_balance
    withdrawal_amount = int(input("please select an amount to withdraw"))
    if withdrawal_amount > acc_balance:
        print("Withdrawal request denied") 
        withdrawal_request()
    else:
        new_balance = acc_balance - withdrawal_amount
        print("New account balance: {}".format(new_balance))
        acc_balance = new_balance
        #dispense_cash()
        print("Have a nice day")
security_check()