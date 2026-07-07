# Write a program which accept number from user and print that number of * in screen

def Display(No):
    for i in range(No):
        print("*")

def main():
    Value = int(input("Enter number : "))

    Display(Value)
       
if __name__ == "__main__":
    main() 