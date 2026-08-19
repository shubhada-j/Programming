# Rename 'Math' column to 'Mathematics'

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

    df = df.rename(columns={'Math' : 'Mathematics'})

    print(df)

if __name__ == "__main__":
    main()