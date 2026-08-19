# Count how many students are passed

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

    df['Total'] = df['Math'] + df['Science'] + df['English']

    df['Status'] = df['Total'].apply(
        lambda total : 'Pass' if total >= 250 else 'Fail'
    )

    Count = 0

    for status in df['Status']:
        if status == 'Pass':
            Count = Count + 1

    print("Passed students are : ",Count)

if __name__ == "__main__":
    main()