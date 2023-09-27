#---------M-ATM----------
print("------Welcome to M-ATM------")
cash=1000
print("Select the option\n1.Deposit\n2.Withdraw\n3.Check balance")
choice=int(input("Enter the option:"))
#Deposit part
if choice==1:
    deposit=float(input("Enter a amount to deposit:"))
    cash=cash+deposit
    option=input("Do you want to receipt Y/N")
    if option=='Y' or option=='y':
        print("\n\tM-ATM\nDate:28/09/2023\nDeposited Amount:",deposit,"\nAvailable balance:",cash,"\n\tThankyou :)")
    else:
        print("Available balance in Your account:",cash)
        print("Thankyou for visiting M-ATM\nHave a nice day :)")
#Withdraw part
elif choice==2:
        withdraw=float(input("Enter a amount to withdraw:"))
        if cash>=withdraw:
            cash=cash-withdraw
            option=input("Do you want to receipt Y/N")
            if option=='Y' or option=='y':
                print("\n\tM-ATM\nDate:28/09/2023\nAvailable balance:",cash,"\nWithdraw Amount:",withdraw,"\n\tThankyou :)")
            else:
                print("Available balance in Your account:",cash)
                print("Thankyou for visiting M-ATM\nHave a nice day :)")
        else:
            print("Insufficient Balance :(\nAvailable balance:",cash)
#Balance checking Part
elif choice==3:
    print("Current balance :",cash)
    option=input("Do you want to receipt Y/N")
    if option=='Y' or option=='y':
        print("\n\tM-ATM\nDate:28/09/2023\nAvailable balance:",cash,"\n\tThankyou :)")
    else:
        print("Available balance in Your account:",cash)
        print("Thankyou for visiting M-ATM\nHave a nice day :)")
else:
    print("Sorry :( check the option")

            

            
            
        
    
