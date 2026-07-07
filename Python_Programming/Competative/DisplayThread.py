""" 
Design a Python application that creates three threads named Small, Capital, and Digits.
All threads should accept a string as input.
The Small thread should count and display the number of lowercase characters.
The Capital thread should count and display the number of uppercase characters.
The Digits thread should count and display the number of numeric digits.
Each thread must also display:
Thread ID
Thread Name
"""

import threading

def Small(Data):
    Count = 0

    print("Inside Small : ",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    
    for ch in Data:
        if(ch >= 'a' and ch <= 'z'):
            print(ch)
            Count = Count + 1
    print("Number of lowercase : ",Count)

def Capital(Data):
    Count = 0

    print("Inside Capital : ",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    for ch in Data:
        if(ch >= 'A' and ch <= 'Z'):
            print(ch)
            Count = Count + 1
    print("Number of uppercase : ",Count)
    
def Digits(Data):
    Count = 0

    print("Inside Digits : ",threading.get_ident())
    print("Thread Name :", threading.current_thread().name)

    for ch in Data:
        if(ch >= '0' and ch <= '9'):
           print(ch)
           Count = Count + 1
    print("Number of Digits : ",Count)

def main():
    Value = str(input("Enter String : "))
    
    t1 = threading.Thread(target=Small, args=(Value,), name="Small")
    t2 = threading.Thread(target=Capital, args=(Value,),name="Capital")
    t3 = threading.Thread(target=Digits,args=(Value,),name="Digits")
    
    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

if __name__ == "__main__":
    main()