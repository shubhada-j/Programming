"""
Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.
Input : Number of elements: 4
Input Elements : 13 5 45 7 
Output: 5
"""

def Minimum(No):
    Ans = min(No)
    return Ans
def main():
    Data = []

    Value = int(input("Enter no. of elements : "))

    for i in range(Value):
        Numbers = int(input("Enter elements : "))
        Data.append(Numbers)

    Ret = Minimum(Data)
    print("Minimum Number : ",Ret)

if __name__ == "__main__":
    main()