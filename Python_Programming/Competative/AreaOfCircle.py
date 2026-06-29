#Write a program which accepts radius of circle and prints area of circle

def CircleArea(Radius):
    PI = 3.14
    Ans = PI * Radius * Radius
    return Ans

def main():
    No = int(input("Enter Radius : "))

    Ret = CircleArea(No)
    print("Area of Circle : ", Ret)

if __name__ ==  "__main__":
    main()