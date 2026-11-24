
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


# Step 1: Load Dataset

df = pd.read_csv("Employee_Attrition (1).csv")


# Step 2: Display Shape, Columns and First Five Records

print("Dataset Shape:")
print(df.shape)

print("\nDataset Columns:")
print(df.columns)

print("\nFirst Five Records:")
print(df.head())


# Step 3: Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())


# Step 4: Identify Numerical and Categorical Features

print("\nNumerical Features:")
print(df.select_dtypes(include=["int64", "float64"]).columns)

print("\nCategorical Features:")
print(df.select_dtypes(include=["object"]).columns)


# Step 5: Convert OverTime into Numerical Form

df["OverTime"] = df["OverTime"].map({
    "No": 0,
    "Yes": 1
})


# Step 6: Convert Attrition into 0 and 1

df["Attrition"] = df["Attrition"].map({
    "No": 0,
    "Yes": 1
})


# Step 7: Separate Independent and Dependent Variables

X = df.drop("Attrition", axis=1)

Y = df["Attrition"]


# Step 8: Split Training and Testing Data

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)


# Step 9: Apply Feature Scaling

Scaler = StandardScaler()

X_train = Scaler.fit_transform(X_train)

X_test = Scaler.transform(X_test)


# Step 10: Design MLP with Two Hidden Layers

MLP = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    activation="relu",
    solver="adam",
    learning_rate_init=0.001,
    max_iter=500,
    early_stopping=True,
    n_iter_no_change=20,
    random_state=42
)


# Step 11: Train the Network

MLP.fit(X_train, Y_train)


# Step 12: Display Number of Iterations

print("\nNumber of Iterations:")
print(MLP.n_iter_)


# Step 13: Calculate Training Accuracy

Train_Prediction = MLP.predict(X_train)

Train_Accuracy = accuracy_score(
    Y_train, Train_Prediction
)

print("\nTraining Accuracy:", Train_Accuracy)


# Step 14: Calculate Testing Accuracy

Test_Prediction = MLP.predict(X_test)

Test_Accuracy = accuracy_score(
    Y_test, Test_Prediction
)

print("\nTesting Accuracy:", Test_Accuracy)


# Step 15: Generate Confusion Matrix

CM = confusion_matrix(
    Y_test,
    Test_Prediction,
    labels=[0, 1]
)

print("\nConfusion Matrix:")
print(CM)

print("\nClassification Report:")
print(classification_report(
    Y_test,
    Test_Prediction,
    zero_division=0
))


# Step 16: Plot Loss Curve

plt.plot(MLP.loss_curve_)

plt.title("MLP Training Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.show()


# Step 17: Create PredictAttrition Function

def PredictAttrition(employee_data):

    if isinstance(employee_data, dict):
        employee_data = [employee_data]

    New_Data = pd.DataFrame(employee_data)

    New_Data["OverTime"] = New_Data["OverTime"].map({
        "No": 0,
        "Yes": 1
    })

    New_Data = Scaler.transform(New_Data)

    Prediction = MLP.predict(New_Data)

    for i in range(len(Prediction)):

        if Prediction[i] == 0:
            print("Employee", i + 1, ": Likely to Stay")

        else:
            print("Employee", i + 1, ": Likely to Leave")


# Step 18: Test Using Five New Employee Records

New_Employees = [
    {
        "Age": 25,
        "MonthlyIncome": 35000,
        "YearsAtCompany": 1,
        "TotalWorkingYears": 3,
        "DistanceFromHome": 40,
        "JobSatisfaction": 1,
        "WorkLifeBalance": 1,
        "OverTime": "Yes",
        "NumCompaniesWorked": 2,
        "TrainingTimesLastYear": 1
    },

    {
        "Age": 45,
        "MonthlyIncome": 95000,
        "YearsAtCompany": 12,
        "TotalWorkingYears": 20,
        "DistanceFromHome": 10,
        "JobSatisfaction": 4,
        "WorkLifeBalance": 3,
        "OverTime": "No",
        "NumCompaniesWorked": 3,
        "TrainingTimesLastYear": 4
    },

    {
        "Age": 29,
        "MonthlyIncome": 50000,
        "YearsAtCompany": 2,
        "TotalWorkingYears": 5,
        "DistanceFromHome": 35,
        "JobSatisfaction": 2,
        "WorkLifeBalance": 2,
        "OverTime": "Yes",
        "NumCompaniesWorked": 4,
        "TrainingTimesLastYear": 2
    },

    {
        "Age": 52,
        "MonthlyIncome": 130000,
        "YearsAtCompany": 18,
        "TotalWorkingYears": 28,
        "DistanceFromHome": 5,
        "JobSatisfaction": 4,
        "WorkLifeBalance": 4,
        "OverTime": "No",
        "NumCompaniesWorked": 2,
        "TrainingTimesLastYear": 5
    },

    {
        "Age": 34,
        "MonthlyIncome": 65000,
        "YearsAtCompany": 5,
        "TotalWorkingYears": 10,
        "DistanceFromHome": 25,
        "JobSatisfaction": 1,
        "WorkLifeBalance": 1,
        "OverTime": "Yes",
        "NumCompaniesWorked": 5,
        "TrainingTimesLastYear": 0
    }
]

PredictAttrition(New_Employees)
