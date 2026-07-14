class BankAccount:

    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount
        
    def Display(self):
        print("Account Holder Name : ",self.Name)
        print("Current Balance : ",self.Amount)

    def Deposit(self):
        self.Amt = float(input("Enter the amount to deposite : "))
        self.Amount = self.Amount + self.Amt
        print("Amount Deposited successfully")

    def Withdraw(self):
        self.Amt = int(input("Enter the amount to withdraw : "))

        if self.Amt <= self.Amount:
            self.Amount = self.Amount - self.Amt
            print("Amount Withdraw Successfully")
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        self.Interest = (self.Amount * BankAccount.ROI) / 100
        return self.Interest

obj1 = BankAccount("Amit",10000)
obj1.Display()
obj1.Deposit()
obj1.Withdraw()
obj1.CalculateInterest()
obj1.Display()