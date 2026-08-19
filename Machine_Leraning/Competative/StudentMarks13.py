# Group Students by gender and calculate average marks

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

    df['Gender'] = ['M','M','F']

    result = df.groupby('Gender')[['Math','Science','English']].mean()

    print(result)     

if __name__ == "__main__":
    main()