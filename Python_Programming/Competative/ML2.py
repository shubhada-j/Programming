# Write a program to Display total number of students in the dataset , Count how many stuents Passed(FinalResult = 1), Count how many stuents Failed(FinalResult = 0)

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("Total number of students : ", len(df))

passed = (df["FinalResult"] == 1).sum()
print("Total number of students passed :",passed)

failed = (df["FinalResult"] == 0).sum()
print("Total number of students failed:",failed)
