# Sort the dataframe by 'Total' marks in descending order

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

    df['Total'] = [252,258,240] 

    df = df.sort_values('Total',ascending=False)

    print(df)

if __name__ == "__main__":
    main()