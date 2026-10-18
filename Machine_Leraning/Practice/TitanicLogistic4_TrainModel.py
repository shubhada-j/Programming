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

# Step 3 : Split Data

#--------------------------------------------------------------
#   Function name : SplitData
#   Description :   It performs spliting activity
#   Input :         Data Frame
#   output :        4 subsets from training and testing
#   Author :        Shubhada Balasaheb Jadhav
#   Date :          16/08/2026
#--------------------------------------------------------------

def SplitData(df):
    X = df.drop("Survived", axis = 1)
    Y = df["Survived"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )

    print("Dataset spliting completed successfully")

    return X_train, X_test, Y_train, Y_test

# Step 3 : Train the Model

#--------------------------------------------------------------
#   Function name : TrainModel
#   Description :   It performs model training
#   Input :         Trainng features and labels
#   output :        Trained model
#   Author :        Shubhada Balasaheb Jadhav
#   Date :          16/08/2026
#--------------------------------------------------------------

def TrainModel(X_train, Y_train):
    model = LogisticRegression(max_iter=1000)

    model = model.fit(X_train, Y_train)

    print("Model Trained Successfully")    

    return model


# Step 3 : Evaluated Data

#--------------------------------------------------------------
#   Function name : EvaluteModel
#   Description :   It performs model testing
#   Input :         model, testing data (features, labels)
#   output :        None
#   Author :        Shubhada Balasaheb Jadhav
#   Date :          16/08/2026
#--------------------------------------------------------------

def EvaluateModel(model, X_test, Y_test):
    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy is : ",accuracy)

    print(confusion_matrix(Y_test,Y_pred))


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

    # Step 3:
    X_train, X_test, Y_train, Y_test = SplitData(df)

    # Step 4:
    model = TrainModel(X_train,Y_train)

    # Step 5:
    EvaluateModel(model, X_test,Y_test)

if __name__ =="__main__":
    main()
