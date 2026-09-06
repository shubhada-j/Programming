import time

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    Value = int(input("Enter the number :"))
    
    start_time = time.perf_counter()    #performance under counter

    Ret = Factorial(Value)
    
    end_time = time.perf_counter()  

    print(f"Factorial of {Value} is {Ret}") #formatted printing
    
    print(f"Time required is : {end_time - start_time : .5f} seconds")

if __name__ == "__main__":
    main()


#use time.perf_counter() because waiting time not calculate in it not use time.time()

"""
Enter the number :10
Factorial of 10 is 3628800
Time required is :  0.00001 seconds
"""