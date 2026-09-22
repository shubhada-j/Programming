import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
