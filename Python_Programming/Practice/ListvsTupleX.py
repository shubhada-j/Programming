#-----------------------------------------
#                List          Tuple
#-----------------------------------------
# ordered        Yes           Yes
# Indexed        Yes           Yes
# Mutable        Yes           No
# Heterogenous   Yes           Yes
#-----------------------------------------
#if data is ordered then it must be indexed and reverse also

def main():
    Data1 = [10,3.14,True,"Pune"]           # List
    Data2 = (10,3.14,True,"Pune")           # Tuple

    print(Data1)
    print(Data2)

    print(Data1[0])
    print(Data2[0])
   

if __name__ == "__main__":
    main()


#important question as per interview

#List,Tuple-> Heterogenus
# Python madhe sagl heterogeneous ast expect string