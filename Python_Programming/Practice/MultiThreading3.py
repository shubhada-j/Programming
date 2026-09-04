# how to pass parameter to thread
# DatatypeX.py refer

import threading        

def Display(No):    # def Display(*No)
    print(f"Inside Display {No}: ",threading.get_ident())

def main():
    print("Inside main : ",threading.get_ident())

    tobj = threading.Thread(target=Display, args=(11,))   #passing parameter (, comma to indicate it is tuple)

    tobj.start()                             

if __name__ == "__main__":
    main()



"""
Inside main :  18552
Inside Display 11:  26160
"""