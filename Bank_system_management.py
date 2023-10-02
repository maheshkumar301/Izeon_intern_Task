import time 
class Transaction:

    def __init__(self,balance=0,count=0):
        self.balance=balance
        self.count=count

    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Successfully credited amount:Rs.{}\n\n".format(amount))
        self.count+=1
        return self.balance

    def withdraw(self,amount):
        if amount<=self.balance :
            self.balance=self.balance-amount
            print("Successfully Debited amount :Rs.{}\n\n".format(amount))
            self.count+=1
            return self.balance
        else:
            print("Insufficient Balance :(\n\n")

    def check_Balance(self):
        print("Available balance:Rs.{}\n\n".format(self.balance))

    def transfer(self,ac):
        try:
            t=int(ac)
            if type(t)==int and len(str(t))==8:
                amount=float(input("Enter amount to transfer:Rs."))
                if amount<=self.balance :
                    self.balance=self.balance-amount
                    print("Successfully Transfered Rs.{} amount to A/c no:{}\n\n".format(amount,ac))
                    self.count+=1
                    return self.balance
                else:
                    print("Insufficient :( ,check the balance\n\n")
            else:
                print("Check the Account Number :(\n\n")
        except:
            print("Enter correct A/c NO :(\n\n")
            
    def Count(self):
        print(self.count)
        return self.count
        
class Loan(Transaction):
    def p_Loan(self):
        print("You Want Personal loan to satisfy 2 condition\n1.Minimum 20,000 keep in your Account\n2.Minimum 5 Transaction complete")
        print("Checking...................................................")
        time.sleep(2)
        if self.balance >= 20000:
            if self.count>=5:
                print("You are eligible to personal loan")
                print("Personal loan interest is 7.5% & amount :Rs.50000")
                op=input("Do you want to take Personal Loan Y/N:")
                if op=='Y' or op=='y' :
                    self.p=50000
                    print("Successfully credited Rs.{} loan amount to your account\n\n".format(self.p))
                    self.balance=self.balance+self.p
                    return self.balance
                else:
                    print("Thankyou\n\n")
            else:
                print("You are not Eligible to personal loan  because Your aren't done minimum transaction\n\n")
    
        else:
            print("You are not eligible to personal loan\n\n")
    def bike_Loan(self):
        print("You Want bike loan to satisfy 2 condition\n1.Minimum 15,000 keep in your Account\n2.Minimum 5 Transaction complete")
        print("Checking...................................................")
        time.sleep(2)
        if self.balance>=15000:
            if self.count>=5:
                print("You are eligible to bike loan")
                print("Bike loan interest is 6.5% & amount :Rs.40000")
                op=input("Do you want to take bike Loan Y/N:")
                if op=='Y' or op=='y' :
                    self.b=40000
                    print("Successfully credited Rs.{} loan amount to your account\n\n".format(self.b))
                    self.balance=self.balance+self.b
                    return self.balance
                else:
                    print("Thankyou\n\n")
            else:
                print("You are not Eligible to bike loan  because Your aren't done minimum transaction\n\n")
        else:
            print("You are not eligible to bike loan\n\n")
    def car_Loan(self):
        print("You Want Car loan to satisfy 2 condition\n1.Minimum 30,000 keep in your Account\n2.Minimum 5 Transaction complete")
        print("Checking...................................................")
        time.sleep(2)
        if self.balance>=30000:
            if self.count>=5:
                print("You are eligible to car loan")
                print("Car loan interest is 5.5% & amount :Rs.65000")
                op=input("Do you want to take Car Loan Y/N:")
                if op=='Y' or op=='y' :
                    self.c=65000
                    print("Successfully credited Rs.{} loan amount to your account\n\n".format(self.c))
                    self.balance=self.balance+self.c
                    return self.balance
                else:
                    print("Thankyou\n\n")
            else:
                print("You are not Eligible to car loan  because Your aren't done minimum transaction\n\n")
        else:
            print("You are not eligible to car loan\n\n")
            
    def home_Loan(self):
        print("You Want home loan to satisfy 2 condition\n1.Minimum 45,000 keep in your Account\n2.Minimum 5 Transaction complete")
        print("Checking...................................................")
        time.sleep(2)
        if self.balance>=45000:
            if self.count>=5:
                print("You are eligible to home loan")
                print("Home loan interest is 4.5% & amount :Rs.100000")
                op=input("Do you want to take home Loan Y/N:")
                if op=='Y' or op=='y' :
                    self.h=100000
                    print("Successfully credited Rs.{} loan amount to your account\n\n".format(self.h))
                    self.balance=self.balance+self.h
                    return self.balance
                else:
                    print("Thankyou\n\n")
            else:
                print("You are not Eligible to home loan  because Your aren't done minimum transaction\n\n")
        else:
            print("You are not eligible to home loan\n\n")

    def pay_Loan(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print("Successfully loan paid")
            return self.balance
        else:
            print("check the amount")
        

while True:
    print("---------Welcome to Mk_BANK :) ----------")
    s=int(input("Do you continue ENTER 1 OR exit ENTER 2 :"))
    print()
    o=Loan()
    if s==1:
        try:
            ch=0
            while True: 
                print("\n---#-----Welcome to Mk_BANK :) ----#-----")
                print("*****choose the option*****")
                print("1.Deposit\n2.Withdraw\n3.Check Balance\n4.Transfer\n5.Loans\n6.Quit")
                ch=int(input("Enter the option:\n"))
                if ch==1:
                    amount=float(input("Enter the amount to deposit:Rs."))
                    o.deposit(amount)
                elif ch==2:
                    amount=float(input("Enter the amount to withdraw:Rs."))
                    o.withdraw(amount)
                elif ch==3:
                    o.check_Balance()
                elif ch==4:
                    ac=int(input("Enter the A/c no to transfer:"))
                    o.transfer(ac)
                elif ch==5:
                    o.Count()
                    ch1=0
                    while True:
                        print("------Available Loans in our bank------")
                        print("1.Personal Loan\n2.Bike Loan\n3.Car Loan\n4.Home Loan\n5.pay Loan\n6.previous\n")
                        ch1=int(input("Enter the option:\n"))
                        if ch1==1:
                            o.p_Loan()
                        elif ch1==2:
                            o.bike_Loan()
                        elif ch1==3:
                            o.car_Loan()
                        elif ch1==4:
                            o.home_Loan()
                        elif ch1==5:
                            amount=float(input("Enter a amount to pay:Rs."))
                            o.pay_Loan(amount)
                        elif ch1==6:
                            break
                else:
                    break
        except:
            print("Invalid data")
    elif s==2:
        break
    else:
        continue
        


