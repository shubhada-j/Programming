"""
Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.
Input : Number of elements: 7
Input Elements : 13 5 45 7 4 56 34  
Output: 56
"""

def Maximum(No):
    Ans = max(No)
    return Ans
def main():
    Data = []

    Value = int(input("Enter no. of elements : "))

    for i in range(Value):
        Numbers = int(input("Enter elements : "))
        Data.append(Numbers)

    Ret = Maximum(Data)
    print("Maximum Number : ",Ret)

if __name__ == "__main__":
    main()