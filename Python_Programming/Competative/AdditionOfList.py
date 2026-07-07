'''
Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.
Input: Number of elements: 6
Input Elements: 13
                5
                45
                7
                4
                56
Output        : 130
'''

def Addition(Numbers):
    Sum = 0

    for Value in Numbers:
        Sum = Sum + Value
    return Sum

def main():
    Data = []

    No = int(input("Enter the no. of elements : "))

    for i in range(No):
        Value = int(input("Enter Element : "))
        Data.append(Value)

    Ret = Addition(Data)
    print("Addition of elements : ",Ret)

if __name__ == "__main__":
    main()
    