# 6! : 1 * 2 * 3 * 5 * 6

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    Value = int(input("Enter the number :"))
    
    Ret = Factorial(Value)
    
    print(f"Factorial of {Value} is {Ret}") #formatted printing

if __name__ == "__main__":
    main()


"""
C:\Users\mdman\Desktop\Python>python TimeCalculations2.py
Enter the number :5
Factorial of 5 is 120
"""