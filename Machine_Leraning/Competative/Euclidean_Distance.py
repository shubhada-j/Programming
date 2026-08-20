# Write python program to calculate the distance between two points before and after applying feature scaling, and explain the difference in results

import numpy as np
import math
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import train_test_split

def main():
    Data = [
        {'X' : 25, 'Y' : 20000},
        {'X' : 30, 'Y' : 40000},
        {'X' : 35, 'Y' : 80000}
    ]

    EucDistance_Data = math.sqrt(
        (Data[0]['X'] - Data[2]['X']) **2 +
        (Data[0]['Y'] - Data[2]['Y']) **2
        )

    print("Before : ",EucDistance_Data)

    Data = np.array([
            [25,20000],
            [30,40000],
            [35,80000]
        ])

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(Data)

    print("Scaled Data : ",scaled_data)

    EucDistance_Data = math.sqrt(
        (scaled_data[0][0] - scaled_data[2][0]) **2 +
        (scaled_data[0][1] - scaled_data[2][1]) **2
        )

    print("After : ",EucDistance_Data)
    
if __name__ == "__main__":
    main()