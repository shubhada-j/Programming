# Display students who scared more than 85 in Science

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

    result = df[df['Science'] > 85]

    print(result[['Name','Science']])
    
if __name__ == "__main__":
    main()
