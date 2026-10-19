import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def main():
    # Step 1 : load the data

    df = pd.read_csv("Mall_Customers.csv")

    print("Dataset loaded with values : ")
    print(df.head());

    print("Missing Values : ")
    print(df.isnull().sum())

    # Step 2 : Feature Selection

    X = df[["AnnualIncome","SpendingScore"]]

    print("Selected Featuires are : ")
    print(X.head())

if __name__ =="__main__":
    main()