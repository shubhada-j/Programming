# division of two numbers concept: exception handling

def main():
    Ans = 0

    try:

      print("Enter first number : ")
      No1 = int(input())

      print("Enter second number : ")
      No2 = int(input())

      Ans = No1 / No2

      print("Division is successfull")

    except ZeroDivisionError as zobj:
       print("Exception occur due to 2nd operand (No2) is 0 : ",zobj)

    except ValueError as vobj:
       print("Exception occured due to invalid datatype : ",vobj)

    print("Result is : ",Ans)

if __name__ =="__main__":
    main()

"""
Enter first number :
12
Enter second number :
4
Division is successfull
Result is :  3.0

C:\Users\mdman\Desktop\Python>python 124ExceptionDemo3.py
Enter first number :
12
Enter second number :
0
Exception occur due to 2nd operand (No2) is 0 :  division by zero
Result is :  0

C:\Users\mdman\Desktop\Python>python 124ExceptionDemo3.py
Enter first number :
12
Enter second number :
h
Exception occured due to invalid datatype :  invalid literal for int() with base 10: 'h'
Result is :  0
"""
