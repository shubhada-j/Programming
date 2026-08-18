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

    max_sciencemarks = df['Science'].max()

    print("Maximum Marks of Science : ",max_sciencemarks)

if __name__ == "__main__":
    main()