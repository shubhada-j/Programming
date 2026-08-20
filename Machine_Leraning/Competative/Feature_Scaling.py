# Write a Python Program using standardscaler to perform feature scaling on the following dataset

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split

def main():
    Data = np.array([
        [25,20000],
        [30,40000],
        [35,80000]
    ])

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(Data)

    print("Scaled Data : ",scaled_data)

if __name__ == "__main__":
    main()