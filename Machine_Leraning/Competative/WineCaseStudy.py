# Wine Case Study
# We have to design Machine learning application which uses Classification technique
# 1. Get Data
# 2. Clean, Prepare and Manipulate Data
# 3. Train Data
# 4. Test Data
# 5. Calculate Accuracy

import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import StandardScaler

def Classifier(DataPath):
    Border = "-"*70

    # Step 1 : Get Data

    print(Border)
    print("Step 1 : Get Data")
    print(Border)

    df = pd.read_csv("WinePredictor.csv")

    print("Load the data successfully")
    print(Border)

    # Step 2 : Clean, Prepare and Manipulate Data 

    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate Data ")
    print(Border)
    
    print(Border)
    print("Clean Data")
    print(Border)

    df.dropna(inplace=True)

    print("Shape of Dataset : ",df.shape)
    print("Total records : ",df.shape[0])
    print("Total Columns : ",df.shape[1])
    print(Border)

    print(Border)
    print("Prepare Data")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    print(Border)

    print(Border)
    print("Input columns : ",X.columns.tolist())
    print("Output columns : Class")
    print(Border)

    # Split the Dataset for training teetsing"

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(Border)
    print("Details of Training and Testing Data")
    print(Border)

    print("Shape of X_train : ",X_train.shape)
    print("Shape of X_test : ",X_test.shape)
    print("Shape of Y_train: ",Y_train.shape)
    print("Shape of Y_test : ",Y_test.shape)

    scalar = StandardScaler()
    
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.fit_transform(X_test)

    print(Border)

    # 3. Train Data
    # 4. Test Data
    # 5. Calculate Accuracy

    print(Border)
    print("Step 5 : Calculate Accuracy")
    print(Border)
   
    accuracy_scores = []
    K_values = range(1,21)

    for k in K_values:
        model = KNeighborsClassifier(n_neighbors=k)
        model = model.fit(X_train_scaled,Y_train)
        Y_pred = model.predict(X_test_scaled)
        accuracy = accuracy_score(Y_test,Y_pred)
        accuracy_scores.append(accuracy)
    print("Accuracy report")    

    for no in accuracy_scores:
        print(no)

    print(Border)

def main():
    Classifier("WinePredictor.csv")

if __name__ == "__main__":
    main()


