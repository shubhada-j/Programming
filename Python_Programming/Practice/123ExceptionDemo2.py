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

    print("Result is : ",Ans)

if __name__ =="__main__":
    main()

"""
C:\Users\mdman\Desktop\Python>python 123ExceptionDemo2.py
Enter first number :
12
Enter second number :
0
Exception occur due to 2nd operand (No2) is 0 :  division by zero
Result is :  0

Enter first number :
12
Enter second number :
12
Division is successfull
Result is :  1.0

Enter first number :
12
Enter second number :
h
Traceback (most recent call last):
  File "C:\Users\mdman\Desktop\Python\123ExceptionDemo2.py", line 25, in <module>
    main()
    ~~~~^^
  File "C:\Users\mdman\Desktop\Python\123ExceptionDemo2.py", line 13, in main
    No2 = int(input())
ValueError: invalid literal for int() with base 10: 'h'
"""