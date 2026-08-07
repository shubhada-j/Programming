# Write a python program to load the file student_performance_ml.csv using pandas. 
# Display : First 5 records, Last 5 records, Total number of rows amd columns, List of column names, Data type of each column 

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("dataset loaded Succesfully")

print("\nFirst 5 records : ")
print(df.head())

print("\nLast 5 records : ")
print(df.tail())

print("Total number of rows and columns : ")
print(df.shape)

print("\nColumn Names : ")
print(df.columns)

print("Data type of each column : ")
print(df.dtypes)