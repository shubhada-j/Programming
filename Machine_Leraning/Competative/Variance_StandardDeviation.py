# Write a Python program that calculates the variance and standard deviation  of dataset for the following values : [6,7,8,9,10,11,12]

import numpy as np

def main():
    Data = [6,7,8,9,10,11,12]

    variance_data = np.var(Data)

    print("Variance of Data is : ",variance_data)

    Standard_Deviation = np.std(Data)

    print("Standard Deviation is : ",Standard_Deviation)

if __name__ == "__main__":
    main()