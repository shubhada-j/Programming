import sys

if(len(sys.argv) == 3):         #3->file name , 2 arguments
    No1 = int(sys.argv[1])
    No2 = int(sys.argv[2])

    Ans = No1 + No2

    print("Addition is : ",Ans)   
else:
    print("Invalid number of arguments")   


"""
C:\Users\mdman\Desktop\Python>python CommandLine5.py
Invalid number of arguments

C:\Users\mdman\Desktop\Python>python CommandLine5.py 10
Invalid number of arguments

C:\Users\mdman\Desktop\Python>python CommandLine5.py 10 11
Addition is :  21

"""