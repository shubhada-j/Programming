# Write a program which display first 10 even numbers on screen

def Display():
    for no in range(2,21,2):
        if(no % 2 == 0):
            print(no)

def main():
    Display()
    
if __name__ == "__main__":
    main()