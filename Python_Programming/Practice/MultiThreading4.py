# how to pass multiple parameters to thread
# refer DataypeX.py 

import threading        

def Display(No1, No2, No3):    # def Display(*No)
    print(f"Inside Display {No1}, {No2}, {No3} : ",threading.get_ident())

def main():
    print("Inside main : ",threading.get_ident())

    tobj = threading.Thread(target=Display, args=(11,21,51,))   #passing multiple parameters

    tobj.start()                             

if __name__ == "__main__":
    main()

"""
Inside main :  26840
Inside Display 11, 21, 51 :  12916
"""