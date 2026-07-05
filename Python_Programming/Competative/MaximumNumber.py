# Write a lambda function using reduce() which accepts a list of numbers and returns the maximum number

from functools import reduce

Maximum = lambda No1,No2: max(No1,No2)

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    
    for i in range(size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    RData = reduce(Maximum,Data)

    print("Maximum number is : ",RData)

if __name__ == "__main__":
    main()