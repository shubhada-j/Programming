"""
Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.
Input: Number of elements: 11
Input Elements: 13 5 45 7 4 56 5 34 2 5 65
Element to search: 5
Output: 3
"""
def Frequency(List,No):
    Count = 0
    for Value in List:
        if(Value == No):
            Count = Count + 1
        
    return Count     

def main():
    Data = []

    No = int(input("Enter the no. of elements : "))

    for i in range(No):
        Value = int(input("Enter Element : "))
        Data.append(Value)

    Number = int(input("Enter the number which we hae to count : "))

    Ret = Frequency(Data,Number)
    print("Frequency is : ",Ret)

if __name__ == "__main__":
    main()