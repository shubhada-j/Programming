# Write a lambda function using filter() which accepts a list of numbers and returns a list of odd numbers.

OddNumber = lambda No : (No % 2 != 0)

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    
    for i in range(size):
        Value = int(input("Enter number : "))
        Data.append(Value)
        
    FData = list(filter(OddNumber,Data))

    print("Odd numbers are : ",FData)

if __name__ == "__main__":
    main()