# dataset load from csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

Border = "-"*30

#####################################################
# Step 1 : Load the Dataset
#####################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DataPath = "iris.csv"                   #relative path  # DataPath Variable banvun tyamadhe path store kela

df = pd.read_csv(DataPath)                        #df-> DataFrame, pd-> pandas, read -_csv-> read the csv

print("dataset loaded Succesfully")
print("Initial Enteries from dataset are :")
print(df.head())

######################################################
# Step 2 : Data Analysis (EDA)
######################################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of Dataset : ",df.shape)           # shape -> property

print("Column names : ",list(df.columns))

print("Missing Values per column :")
print(df.isnull().sum())                        #conanical function call 

print("Class Distribution (species count)")
print(df["species"].value_counts())

print("Stastical report of dataset : ")
print(df.describe())

#######################################################
# Step 3 : Decide Independent and depenedet variables
#######################################################

print(Border)
print("Step 3 : Decide Independent and depenedet variables")
print(Border)

# X : Independet Variables / Features
# Y : Dependent Variables / Label

feature_cols = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]

X = df[feature_cols]            # 150 by 4 
Y = df["species"]               # 150 by 0        

print("X Shape : ", X.shape)
print("Y Shape : ", Y.shape)

#######################################################
# Step 4 : Visualisation of Dataset
#######################################################

print(Border)
print("Step 4 : Visualisation of Dataset")
print(Border)

#Scattered plot
plt.figure(figsize=(7,5))

for sp in df["species"].unique():
    temp = df[df["species"] == sp]
    plt.scatter(temp["petal length (cm)"], temp["petal width (cm)"],label = sp)

plt.title("Marvellous Iris Case Study")

plt.xlabel("petal length (cm)")
plt.xlabel("petal width (cm)")

plt.legend()
plt.grid()
plt.show()

#######################################################
# Step 5 : Split the dataset for traning and testing
#######################################################

print(Border)
print("Step 5 : Split the dataset for traning and testing")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

print("Dataset Spliting acitvity done")

print("X : ",X.shape)               # (150, 4)
print("Y : ",Y.shape)               # (150, 0)

print("X_train : ",X_train.shape)   # (75, 4)
print("X_test : ",X_test.shape)     # (75, 4)

print("Y_train : ",Y_train.shape)   # (75, )
print("Y_test : ",Y_test.shape)     # (75, )


#######################################################
# Step 6 : Build the model
#######################################################

print(Border)
print("Step 6 : Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

print("Model gets created successfully")

#######################################################
# Step 7 : Train the model
#######################################################

print(Border)
print("Step 7 : Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model trained successfully")

#######################################################
# Step 8 : Test the model
#######################################################

print(Border)
print("Step 8 : Test the model")
print(Border)

Y_pred = model.predict(X_test)

print("Model Testing done")

print("Expected Answers : ")
print(Y_test)

print("Predicted Ansers : ")
print(Y_pred)

#######################################################
# Step 9 : Evaluate the model performance
#######################################################

print(Border)
print("Step 9 : Evaluate the model performance")
print(Border)

accuracy = accuracy_score(Y_test, Y_pred)
print("Accuracy of Model is : ",accuracy*100)

print("Confusion Matrix :")
cm = confusion_matrix(Y_test, Y_pred)
print(cm)

print("Classification Report")
print(classification_report(Y_test, Y_pred))
