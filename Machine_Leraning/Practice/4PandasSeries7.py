import pandas as pd
 

def main():
    sobj = pd.Series([27000,32000,35000],index = ["Amit","Sagar","Sagar"])       
    print(sobj)

    print(sobj["Sagar"])

if __name__ == "__main__":
    main()


 # index chi nav 
 # case sensitive
 # you can create any row with any index 
 # cannot use duplicate index its must be unique because it is like key : value but if we give same index then it accept and shows both values in output