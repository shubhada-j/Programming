import pandas as pd

Border = "-"*30

#############################################
# Step 1 : Load the Dataset
#############################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

DataPath = "iris.csv"                  

df = pd.read_csv(DataPath)                       

print("dataset loaded Succesfully")
print("Initial Enteries from dataset are :")
print(df.head())
