# Normalize the 'Math' scores using Min-Max scaling

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

    min_value = df['Math'].min()
    max_value = df['Math'].max()

    print(min_value)
    print(max_value)

    df['math_normalized_value'] = (df['Math'] - min_value) / (max_value - min_value)

    print(df[['Name','Math','math_normalized_value']])     

if __name__ == "__main__":
    main()