# Write a lambda function using filter() which accepts a list of strings and returns a list of strings having greater than 5.


StringLength = lambda String : len(String) > 5

def main():
    size = int(input("Enter number of elements: "))

    Data = []
    
    for i in range(size):
        Value = input("Enter String : ")
        Data.append(Value)

    FData = list(filter(StringLength,Data))

    print("Strings having length greater than 5 :",FData)

if __name__ == "__main__":
    main()