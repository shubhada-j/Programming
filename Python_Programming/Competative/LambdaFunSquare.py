"""
Write a program which contains one lambda function which accepts one parameter and return power of two.
Input: 4
Output: 16
Input: 8
Output: 64
"""
Square = lambda No : No * No
def main():
    Value = int(input("Enter number : "))

    Ret = Square(Value)

    print("Power of two is : ",Ret)
    
if __name__ == "__main__":
    main()