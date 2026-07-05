# Write a lambda function using map() which accepts a list of numbers and returns a list of square of each number.

SquareNumber = lambda No : (No * No)

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    
    for i in range(size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    MData = list(map(SquareNumber,Data))

    print("Square of numbers : ",MData)

if __name__ == "__main__":
    main()