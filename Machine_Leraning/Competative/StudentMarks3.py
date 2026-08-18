# Add a new column 'Total' to the DataFrame as the sum of all subject marks
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

    print(df)

    # add column in DataFrame
    df['Total'] = [252,258,240]         

    print(df)

if __name__ == "__main__":
    main()