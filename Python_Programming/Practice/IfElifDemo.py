print("---------------------------------------")
print("--------Ticket Pricing Software--------")
print("---------------------------------------")

print("Enter your Age : ")
Age = int(input())

if(Age <= 5):
    print("Free entry")
elif((Age > 5) and (Age <= 18 )):
    print("Ticket price : 900")
elif((Age > 18) and (Age <= 40)):
    print("Ticket Price : 1200")
else:
    print("Ticket Price : 500")
