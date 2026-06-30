# Write a program which accept one character and 
# checks whether it is vowel or consonant

def Character(Value):
    if((Value == 'A') or (Value == 'E') or (Value == 'I') or (Value == 'O') or (Value == 'U') or 
       (Value == 'a') or (Value == 'e') or (Value == 'i') or (Value == 'o') or (Value == 'u')):
        return True
    else:
        return False
        
          
def main():
    Letter = input("Enter character : ")

    Ret = Character(Letter)

    if(Ret == True):
        print("It is Vowel")
    else:
        print("It is Consonant")
    
if __name__ ==  "__main__":
    main()
