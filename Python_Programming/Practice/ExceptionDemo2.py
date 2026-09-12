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