import threading        #name of module

def Display():
    print("Inside Display : ",threading.get_ident())


def main():
    print("Inside main : ",threading.get_ident())
    Display()

if __name__ == "__main__":
    main()

"""
only one thread -> main

o/p:
Inside main :  3156
Inside Display :  3156

ouput in both same beacuse only one thread
"""