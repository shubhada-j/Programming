# division of two numbers concept: exception handling

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    Ans = No1 / No2
    
    print("Result is : ",Ans)

if __name__ =="__main__":
    main()

"""
Enter first number :
12
Enter second number :
4
Result is :  3.0

C:\Users\mdman\Desktop\Python>python 122ExceptionDemo1.py
Enter first number :
12
Enter second number :
12
Result is :  1.0

C:\Users\mdman\Desktop\Python>python 122ExceptionDemo1.py
Enter first number :
12
Enter second number :
0
Traceback (most recent call last):
  File "C:\Users\mdman\Desktop\Python\122ExceptionDemo1.py", line 21, in <module>
    main()
    ~~~~^^
  File "C:\Users\mdman\Desktop\Python\122ExceptionDemo1.py", line 11, in main
    Ans = No1 / No2
          ~~~~^~~~~
ZeroDivisionError: division by zero
(exception name)   (exception cause)
"""