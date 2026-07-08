""" 
Design a Python application that creates two threads.
Thread 1 should compute the sum of elements from a list.
Thread 2 should compute the product of elements from the same list.
Return the results to the main thread and display them.
"""
import threading

def Sum(List):
    Sum = 0

    for Value in List:
        Sum = Sum + Value

    print("Summation is : ",Sum)

def Product(List):
    Mult = 1

    for Value in List:
        Mult = Mult * Value

    print("Product is : ",Mult)

def main():
    size = int(input("Enter no. of elements : "))

    Data = []

    for i in range(size):
        Value = int(input("Enter a number : "))
        Data.append(Value)

    t1 = threading.Thread(target=Sum, args=(Data,))
    t2 = threading.Thread(target=Product, args=(Data,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()