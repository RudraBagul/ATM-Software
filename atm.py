class ATM:
    def __init__(self):
        self.__pin=""
        self.__balance=0

        self.menu()

    def menu (self):
        user_menu=input("""
welcome to ATM please enter 
1. Enter 1 for entering pin
2. Enter 2 for diposit
3. Enter 3 for withdraw
4. Enter 4 for see balance
5. Enter 5 to exit
""")
 
        if user_menu=="1":
            self.set_pin()
        elif user_menu=="2":
            self.dep_amount()
        elif user_menu=="3":
            self.with_draw()
        elif user_menu=="4":
            self.check_balance()
        elif user_menu=="5":
            print("Thankyou for transections")
        else:
            print("Invalid pin")
        print()

    def set_pin (self):
        print()
        self.__pin=input("Enter pin:")
        print()
        if len(self.__pin)==4:
            print("Pin set sussesfully")
            print()
            self.new_menu()
            print()
        else:
            print("Pin should be of 4 digits only")
            print("Try again")
            print()

    def dep_amount(self):
        if len(self.__pin)==0:
            print()
            print("First set pin")
            self.__pin=input("Enter pin:")
            print()
            if len(self.__pin)==4:
                print()
            else:
                print("Pin should be of 4 digits only")
                print("Try again")
                print()
        else:
            print()
            pin=input("Enter pin:")
            if pin==self.__pin:
                amount=int(input("Enter money:"))
                self.__balance+=amount
                print()
                print(f"Your balance is Rs{self.__balance}")
                print()
            else:
                print()
                print("Invalid pin")
                print()
        self.new_menu()

    def with_draw (self):
        if len(self.__pin)==0:
            print()
            print("First set pin ")
            print()
            self.__pin=input("Enter pin:")
            if len(self.__pin)==4:
                print()
            else:
                print("Pin should be of 4 digits only")
                print("Try again")
                print()
        else:
            print()
            pin=input("Enter pin:")
            if pin==self.__pin:
                amount=int(input("Enter the withdraw amount:"))
                print()
                if amount<=self.__balance:
                    self.__balance-=amount
                    print()
                    print(f"Your balence is {self.__balance}")                    
                    print()
                else:
                    print("Invalid amount")
                    print()
            else:
                    print("Invalid pin")
                    print()
        self.new_menu()

    def check_balance (self):
        if len(self.__pin)==0:
            print()
            print("First set pin ")
            self.__pin=input("Enter pin:")
            print()
            if len(self.__pin)==4:
                print()
            else:
                print("Pin should be of 4 digits only")
                print("Try again")
                print()
        else:
            print(f"Your balence is {self.__balance}")
            print()
        self.new_menu()

    def new_menu(self):
        users_menu=input("""
welcome to ATM please enter 
1. Enter 1 for diposit
2. Enter 2 for withdraw
3. Enter 3 for see balance
4. Enter 4 to exit
""")    
           
        if users_menu=="1":
            self.dep_amount()
        elif users_menu=="2":
            self.with_draw()
        elif users_menu=="3":
            self.check_balance()
        elif users_menu=="4":
            print("thankyou for transections")
        else :
            print("invalid pin")
sbi=ATM()
