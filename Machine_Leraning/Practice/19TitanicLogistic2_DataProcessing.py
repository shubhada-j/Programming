import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

# Step 1 : Load Data

#--------------------------------------------------------------
#   Function name : LoadData
#   Description :   Load the data from CSV
#   Input :         Name of CSV file
#   output :        Data frame
#   Author :        Shubhada Balasaheb Jadhav
#   Date :          16/08/2026
#--------------------------------------------------------------

def LoadData(fileName):
    df = pd.read_csv(fileName)
    
    print("Dataset loaded successfully")
    print(df.head())

    return df

# Step 2 : Data Proceessing

#--------------------------------------------------------------
#   Function name : PreProcessData
#   Description :   It perform data analaysis
#   Input :         Data Frame
#   output :        Updated Data frame
#   Author :        Shubhada Balasaheb Jadhav
#   Date :          16/08/2026
#--------------------------------------------------------------

def PreProcessData(df):
    df = df.drop([
        "zero",
        "Passengerrid",
        "name"
    ],
    errors = "ignore"
    )

    # Handle Mising Values 

    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Fare"] = df["Fare"].fillna(df["Fare"].median())

    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Convert categorical to numeric data
    df = pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int
    )

    print(df.head())

    print("Data Preprceessing Completed")

    return df

#--------------------------------------------------------------
#   Function name : Main
#   Description :   Entry Point Function
#   Input :         None
#   output :        None
#   Author :        Shubhada Balasaheb Jadhav
#   Date :          16/08/2026
#--------------------------------------------------------------

def main():
    # Step 1:
   df =  LoadData("MarvellousTitanicDataset.csv")

   # Step 2:
   df = PreProcessData(df)

if __name__ =="__main__":
    main()