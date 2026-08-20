# Write a Python program that calculates the mean of dataset using NumPy for the following values : [6,7,8,9,10,11,12]

import numpy as np

def main():
    Data = [6,7,8,9,10,11,12]

    mean_data = np.mean(Data)

    print("Mean of Data is : ",mean_data)

if __name__ == "__main__":
    main()