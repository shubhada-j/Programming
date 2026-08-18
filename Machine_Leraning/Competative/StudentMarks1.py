# Create a DataFrame for student and marks and ptrint basic information like shape, columns and data types.

import pandas as pd
import numpy as np


def main():
    Data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(Data) 
    
    print("Shape of DataFrame : ",df.shape)          # no. of rows and columns
    print("Columns are : ",df.columns)               # columns
    print("Data Types are : \n",df.dtypes)             # data type

if __name__ == "__main__":
    main()