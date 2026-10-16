import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

def Marvellousregression(Datapath):
    Border = "-"*70

    # Step 1 : load the Data
    print(Border)
    print("Step 1 : load the Data")
    print(Border)

    df = pd.read_csv(Datapath)

    print(df.head)

def main():
    Marvellousregression("Advertising.csv")


if __name__ == "__main__":
    main()