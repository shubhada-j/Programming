import pandas as pd

Border = "-"*30

#####################################################
# Step 1 : Load the Dataset
#####################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DataPath = "iris.csv"                   

df = pd.read_csv(DataPath)                     

print("dataset loaded Succesfully")
print("Initial Enteries from dataset are :")
print(df.head())

######################################################
# Step 2 : Data Analysis (EDA)
######################################################

print(Border)
print("Step 2 : Data Analysis (EDA)")
print(Border)

print("Shape of Dataset : ",df.shape)           

print("Column names : ",list(df.columns))

print("Missing Values per column :")
print(df.isnull().sum())                        

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

X = df[feature_cols]           
Y = df["species"]                    

print("X Shape : ", X.shape)
print("Y Shape : ", Y.shape)
