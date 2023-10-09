#Shopping Mall
#Register
def register():
        fp=open('try.csv','a')
        try:
            print("------------REGISTER---------------")
            a=input("Enter Your Name:")
            b=int(input("Enter mobile number:"))
            if len(a)>0 and len(str(b))==10:
                print("Note:password will be minimum 6 character")
                c=input("Enter a password:")
                d=input("Confirm password:")
                if len(c)==len(d)>=6 and c==d:
                    fp.write(f"{a},{b},{c}\n")
                    print("Successfully Registered")
                    return True
                else:
                    print("check your password")
                    return False
            else:
                print("check your name or mobile number")
                return False
        except:
            print("Enter valid data")
        else:
            fp.close()
#Login
def login():
    try:
        with open('try.csv') as f:
            l=f.readlines()
            k=[]
            for i in l:
                k.append(i.split(','))
            m,n=[],[]
            for a in k:
                m.append(a[1])
                n.append(a[2].strip())
            o=dict(zip(m,n))
            print("------------LOGIN------------")
            try:
                p=int(input("Enter your mobile number:"))
                if str(p) in o:
                    q=input("Enter password:")
                    if (o.get(str(p)))== q:
                        print("Login Successful :)")
                        return True
                    else:
                        print("check your password :(")
                elif len(str(p))<10:
                    print("Check your mobile number :(")
                else:
                    r=input("You are new user!\nDo you want to register ENTER 1 or quit ENTER 2 :\n")
                    if r=='1':
                        register()
                    else:
                        return False
                    
            except:
                print("Invalid data :(")
    except:
        print("File error")
    else:
        f.close()
#display categories        
def show_Categories():
    print("\n---------------Available Categories:------------------")
    print("1. Electronics\n2. Clothing\n3. Home Appliances\n4. Previous")
#display brands    
def show_Brands(category):
        if category == '1':
                        print("\n----------------Available brands-----------------------")
                        print("1. Sony\n2. Samsung\n3. LG\n4.Back")
                        choice=input("Select the brand:")
                        if choice=='1':
                                print("-------------Sony Products-----------")
                                pdt=['Television','Headphones']
                                dis(pdt)
                                while True:
                                        inp=int(input("Select the product to buy or 3 to quit:"))
                                        if inp==1:
                                                print("You are selected product is {} price:Rs.30000 and discount:20%".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(30000,count,0.2)
                                                pay_Bill()
                                        elif inp==2:
                                                print("You are selected product is {} price:Rs.2000 and discount:10%".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(2000,count,0.1)
                                                pay_Bill()
                                        else:
                                                return False
                        elif choice=='2':
                                print("-------------Samsung Products---------")
                                pdt=['Mobile phones','Laptops','Watches']
                                dis(pdt)
                                while True:
                                        inp=int(input("Select the product to buy or 4 to Quit:"))
                                        if inp==1:
                                                print("You are selected product is {} price:Rs.25000 and discount:20%".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(25000,count,0.2)
                                                pay_Bill()
                                        elif inp==2:
                                                print("You are selected product is {} price:Rs.50000 and discount:30%".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(50000,count,0.3)
                                                pay_Bill()
                                        elif inp==3:
                                                print("You are selected product is {} price:Rs.1000 and discount:12%".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(1000,count,0.12)
                                                pay_Bill()
                                        else:
                                                return False
                        elif choice=='3':
                                print("-------------LG products--------------")
                                pdt=['Computer Monitors','Televisions','Home theater']
                                dis(pdt)
                                while True:
                                        inp=int(input("Select the product to buy or 4 to Quit:"))
                                        if inp==1:
                                                print("You are selected product is {} price:Rs.20000".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(20000,count,0)
                                                pay_Bill()
                                        elif inp==2:
                                                print("You are selected product is {} price:Rs.23000".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(23000,count,0)
                                                pay_Bill()
                                        elif inp==3:
                                                print("You are selected product is {} price:Rs.18000".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(18000,count,0)
                                                pay_Bill()
                                        else:
                                                return False
                        else:
                                return False

        elif category == '2':
                        print("\n----------------Available brands-----------------------")
                        print("1. Allen Solly\n2. Adidas\n3. Back")
                        choice=input("Select the brand:")
                        if choice=='1':
                                print("---------Allen Solly----------")
                                pdt=['Shirts','Pants','T-shirt','Trousers']
                                dis(pdt)
                                
                                while True:
                                        inp=int(input("Select the product to buy or 5 to Quit:"))
                                        if inp==1:
                                                print("You are selected product is {} price:Rs.700".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(700,count,0)
                                                pay_Bill()
                                        elif inp==2:
                                                print("You are selected product is {} price:Rs.1200".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(1200,count,0)
                                                pay_Bill()
                                        elif inp==3:
                                                print("You are selected product is {} price:Rs.300".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(300,count,0)
                                                pay_Bill()
                                        elif inp==4:
                                                print("You are selected product is {} price:Rs.450".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(450,count,0)
                                                pay_Bill()
                                        else:
                                                return False
                        
                        elif choice=='2':
                                print("---------Adidas----------")
                                pdt=['Shirts','Pants','T-shirt','Trousers']
                                dis(pdt)
                                
                                while True:
                                        inp=int(input("Select the product to buy or 5 to Quit:"))
                                        if inp==1:
                                                print("You are selected product is {} price:Rs.650".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(650,count,0)
                                                pay_Bill()
                                        elif inp==2:
                                                print("You are selected product is {} price:Rs.1150".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(1150,count,0)
                                                pay_Bill()
                                        elif inp==3:
                                                print("You are selected product is {} price:Rs.300".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(300,count,0)
                                                pay_Bill()
                                        elif inp==4:
                                                print("You are selected product is {} price:Rs.350".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(350,count,0)
                                                pay_Bill()
                                        else:
                                                return False
                        else:
                                return False
        elif category == '3':
                        print("\n----------------Available brands-----------------------")
                        print("1. Panasonic\n2. Philips\n3. Back")
                        
                        choice=input("Select the brand:")
                        if choice=='1':
                                print("---------Panasonic----------")
                                pdt=['Washing Machine','Refrigerator','Rice Cooker']
                                dis(pdt)
                                
                                while True:
                                        inp=int(input("Select the product to buy or 4 to Quit:"))
                                        if inp==1:
                                                print("You are selected product is {} price:Rs.13990".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(13990,count,0)
                                                pay_Bill()
                                        elif inp==2:
                                                print("You are selected product is {} price:Rs.36990".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(36990,count,0)
                                                pay_Bill()
                                        elif inp==3:
                                                print("You are selected product is {} price:Rs.3156".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(3156,count,0)
                                                pay_Bill()
                                        else:
                                                return False
                        
                        elif choice=='2':
                                print("---------Philips----------")
                                pdt=['Micro Oven','Mixer Grinder','vacuum cleaner']
                                dis(pdt)
                                
                                while True:
                                        inp=int(input("Select the product to buy or 4 to Quit:"))
                                        if inp==1:
                                                print("You are selected product is {} price:Rs.12000".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(12000,count,0)
                                                pay_Bill()
                                        elif inp==2:
                                                print("You are selected product is {} price:Rs.5500".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(5500,count,0)
                                                pay_Bill()
                                        elif inp==3:
                                                print("You are selected product is {} price:Rs.8499".format(pdt[inp-1]))
                                                count=int(input("How many you want:"))
                                                bill(8499,count,0)
                                                pay_Bill()
                                        else:
                                                return False
                        else:
                              return False
        else:
                return False
        
#display products
def dis(pdt):
        for i in range(len(pdt)):
                    print(f"{i+1}:{pdt[i]}")
        
#Total amount
def bill(price,count,discount):
        total=(price*count)-(price*count*discount)
        print("Total Amount:Rs.",total)
#payment
def pay_Bill():
        while True:
                inpt=input("If you wanna pay Y/N:")
                if inpt=='Y' or inpt=='y' :
                        try:
                                card=int(input("Enter your card number:"))
                                if len(str(card))==12:
                                        pin=int(input("Enter your pin:"))
                                        if len(str(pin))==4:
                                                print("Successfully paid :)\n-------------------------------------------------------------------------- ")
                                                return False
                                        else:
                                                print("check the pin")
                                                continue
                                else:
                                        print("check the card number")
                                        continue
                        except:
                                print("Invalid Data")
                else:
                        return False
#main Loop    
while True:
    print("--------------------Welcome to Max Mall---------------------\n1.Register\n2.Login\n3.Quit")
    try:
        op=int(input("Enter option:"))
        if op==1 :
                register()
        elif op==2:
                if login():
                        while True:
                                show_Categories()
                                ch=input("Select the Categories:")
                                show_Brands(ch)
                                if ch=='4':
                                        break
        else:
                break
    except:
            print("Invalid option")
