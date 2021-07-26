class Atm:

    print ("Welcome to the Online Atm")
    CardNo = input ("Please enter your card number: ")
    PinNo = input ("please enter your pin number: ")

    if CardNo = self.cardNumber:
        print ("The card number is correct")

    if PinNo = self.PinNumber:
        print ("yes the pin number is correct")
        

    def __init__(self,name,gender,age,cardNumber,PinNumber,):
        self.name=name
        self.gender=gender
        self.age=age
        self.cardNumber=3496
        self.PinNumber=1058

    def cashWithdraw(self,amount):
    if self.balance-amount > 0:
      self.balance=self.balance-amount
      print("$",amount," withdrawn. Current Balance: $",self.balance)
    else:
      print("You don't have enough money")

    def cashDeposit (self,amount):
        Money = input("How much money would you like to deposit: ")
        self.balance=self.balance+Money
        print ("Yay you deposited $" + Money + "your current balance is $" + self.balance)

    def balanceEnquiry (self,amount):
        BalanceEnquiring = input ("Would like to know how much money you have currently? type YES or NO")
        if BalanceEnquiring = "YES":
            print ("Your current balance is: $" + self.balance)






