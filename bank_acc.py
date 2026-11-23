def deposite(amount):
    if amount<0:
        print("Deposite balance must be greater than 0.")
        return 0
    else:
        print(f"{amount} credited successfully!")
        return amount
    
def withdraw(amount,my_balance):
    if(amount<=my_balance):
        print(f"{amount} debited successfully!")
        return amount
    else:
        print("Insufficient Balance.")
        return 0

def check_balance(my_balance):
    print(f"Your current balance: {my_balance}")
    
my_balance = 0.0
    
def run(my_balance):
    while True:
        print("1) Deposite")
        print("2) Withdraw")
        print("3) check balance")
        print("4) Exit")
        
        opt = input("Choose One Option: ") 
        if(opt=="1"):
            amount = int(input("Enter amount for deposite: "))
            my_balance+=deposite(amount)
            input("Press Enter for continue")
        elif(opt=="2"):
            amount = int(input("Enter amount for withdraw: "))
            my_balance -= withdraw(amount,my_balance)
            input("Press Enter for continue")
        elif(opt=="3"):
            check_balance(my_balance)
            input("Press Enter for continue")
        elif(opt=="4"):
            print("Thanks for visting!")
            break
        else:
            print("Choose correct option.")

run(my_balance)

        


