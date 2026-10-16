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

#--------------------------------------------------------------
#   Function name : Main
#   Description :   Entry Point Function
#   Input :         None
#   output :        None
#   Author :        Shubhada Balasaheb Jadhav
#   Date :          16/08/2026
#--------------------------------------------------------------

def main():
    LoadData("MarvellousTitanicDataset.csv")

if __name__ =="__main__":
    main()