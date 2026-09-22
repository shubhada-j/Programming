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