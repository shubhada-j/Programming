# Play Predictor Case Study
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
from sklearn.preprocessing import StandardScaler, LabelEncoder

def Classifier(DataPath):
    Border = "-"*50

    # Step 1 : Get Data

    print(Border)
    print("Step 1 : Get Data")
    print(Border)

    df = pd.read_csv(DataPath)
    print("Dataset loaded successfully")

    # Step 2 : Clean, Prepare and Manipulate Data

    print(Border)
    print("Step 2 : Clean, Prepare and Manipulate Data")
    print(Border)

    df.dropna(inplace=True)

    print("Shape of Dataset : ",df.shape)
    print("Total Columns : ",df.shape[1])
    print("Total records : ",df.shape[0])
    print(Border)

    X = df.drop(columns=['Play'])
    Y = df['Play']

    encoder = LabelEncoder()

    for columns in X.columns:
        X[columns] = encoder.fit_transform(X[columns].astype(str))

    Y = encoder.fit_transform(Y.astype(str))

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)
    print(Border)


    print("Input Columns : ",X.columns.tolist())
    print("Output columns : ['Play']")
    print(Border)

    # Split the dataset for training and testing

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,random_state=42,test_size=0.2,stratify=Y)

    print("Shape of X_test : ",X_test.shape)
    print("Shape of X_train : ",X_train.shape)
    print("Shape of Y_test : ",Y_test.shape)
    print("Shape of Y_train : ",Y_train.shape)

    scalar = StandardScaler()

    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.transform(X_test)

    # 3. Train Data
    # 4. Test Data
    # 5. Calculate Accuracy

    print(Border)
    print("Step 5 : Calculate Accuracy")
    print(Border)

    accuracy_scores = []
    K_Values = range(1,len(X_train)+1)

    for k in K_Values:
       model = KNeighborsClassifier(n_neighbors=k)
       model = model.fit(X_train_scaled,Y_train)
       Y_pred = model.predict(X_test_scaled)
       accuracy = accuracy_score(Y_test,Y_pred)
       accuracy_scores.append(accuracy)

    print("Accuracy report : ")

    for no in accuracy_scores:
        print(no)

    print(Border)

def main():
    Classifier("PlayPredictor.csv")

if __name__ == "__main__":
    main()