# dataset load from csv

import pandas as pd

Border = "-"*30

#############################################
# Step 1 : Load the Dataset
#############################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DataPath = "iris.csv"                   #relative path  # DataPath Variable banvun tyamadhe path store kela

df = pd.read_csv(DataPath)                        #df-> DataFrame, pd-> pandas, read -_csv-> read the csv

print("dataset loaded Succesfully")
print("Initial Enteries from dataset are :")
print(df.head())

#############################################
# Step 2 : Data Analysis (EDA)
#############################################

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