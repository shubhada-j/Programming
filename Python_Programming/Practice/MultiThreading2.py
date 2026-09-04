# how to make thread

import threading        

def Display():
    print("Inside Display : ",threading.get_ident())


def main():
    print("Inside main : ",threading.get_ident())

    tobj = threading.Thread(target=Display)   #creating thread

    tobj.start()                              #threadla sangitl task kar

if __name__ == "__main__":
    main()

"""
Inside main :  26432
Inside Display :  15972

output is different because there is 2 threads

"""