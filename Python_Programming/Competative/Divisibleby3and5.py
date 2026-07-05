# Write a lambda function using filter() which accepts a list of numbers and returns the list of numbers divisible by both 3 and 5 

Divisible = lambda No: (No % 3 == 0 and No % 5 == 0)

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    
    for i in range(size):
        Value = int(input("Enter number : "))
        Data.append(Value)

    FData = list(filter(Divisible,Data))

    print("Number which are divisible by 3 and 5 are : ",FData)

if __name__ == "__main__":
    main()