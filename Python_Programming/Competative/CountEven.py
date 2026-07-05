# Write a lambda function using filter() which accepts a list of numbers and returns the count of even numbers 

CountEven = lambda No: (No % 2 == 0 )

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    
    for i in range(size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    FData = list(filter(CountEven,Data))

    print("Count of Even Numbers are : ",len(FData))
    print("Even Numbers are : ",FData)

if __name__ == "__main__":
    main()