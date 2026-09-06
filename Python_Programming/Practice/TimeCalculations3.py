import time     #module

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    Value = int(input("Enter the number :"))
    
    start_time = time.time()

    Ret = Factorial(Value)
    
    end_time = time.time()

    print(f"Factorial of {Value} is {Ret}") #formatted printing
    
    print(f"Time required is : {end_time - start_time} seconds")

if __name__ == "__main__":
    main()

"""
Enter the number :10
Factorial of 10 is 3628800
Time required is : 1.0967254638671875e-05 seconds
"""