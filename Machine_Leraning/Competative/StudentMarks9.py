# Create a DataFrame with missing values and fill them with column mean

import pandas as pd
import numpy as np

def main():
    Data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [np.nan,76,78],
        'Science' : [91,np.nan,80]
    }

    df = pd.DataFrame(Data) 

    df['Math'] = df['Math'].fillna(df['Math'].mean())
    df['Science'] = df['Science'].fillna(df['Science'].mean())

    print(df)

if __name__ == "__main__":
    main()