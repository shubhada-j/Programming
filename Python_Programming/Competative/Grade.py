"""
Write a progrsm which acceptd marks and displays grade.
Condition Example:
  >= 75 -> Distinction
  >= 60 -> First Class
  >= 50 -> Second Class
  <50   -> Fail
"""

def Grade(Value):
    if(Value >= 75):
        print("Distinction")
    elif(Value >= 60):
        print("First Class")
    elif(Value >= 50):
        print("Second Class")
    else:
        print("Fail")

def main():
    No = int(input("Enter number : "))

    Grade(No)

if __name__ ==  "__main__":
    main()
