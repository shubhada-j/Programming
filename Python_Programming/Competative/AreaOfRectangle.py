#Write a program which accepts length ande width of rectangle and prints area

def RectangleArea(Length, Breadth):
    Ans = Length * Breadth
    return Ans

def main():
    No1 = int(input("Enter length : "))
    No2 = int(input("Enter breadth : "))

    Ret = RectangleArea(No1,No2)
    print("Area of Rectangle : ", Ret)

if __name__ ==  "__main__":
    main()