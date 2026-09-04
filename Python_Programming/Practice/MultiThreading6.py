import time

# 2+4+6+8 = 20
def SumEven(No):
    Sum = 0

    for i in range(2,No,2):
        Sum = Sum + i

    print("Summation of Even :",Sum)

# 1+3+5+7+9 = 25
def SumOdd(No):
    Sum = 0

    for i in range(1,No,2):
        Sum = Sum + i

    print("Summation of Odd :",Sum)

def main():
    start_time = time.perf_counter()

    SumEven(100000000)
    SumOdd(100000000)       
    
    end_time = time.perf_counter()

    print(f"Time require is : {end_time - start_time : .4f}")
    
if __name__ == "__main__":
    main()

"""
Summation of Even : 2499999950000000
Summation of Odd : 2500000000000000
Time require is :  4.4692

"""