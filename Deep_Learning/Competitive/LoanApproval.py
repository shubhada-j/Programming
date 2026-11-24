import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score


# Step 1: Load Dataset

df = pd.read_csv("Customer_Loan_Approval (1).csv")

print("Dataset:")
print(df.head())

print("Dataset Shape:")
print(df.shape)


# Step 2: Check Missing Values

print("Missing Values:")
print(df.isnull().sum())


# Step 3: Separate Input and Output Variables

X = df.drop("LoanApproved", axis=1)

Y = df["LoanApproved"]


# Step 4: Split Training and Testing Data

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)


# Step 5: Train Logistic Regression

LR = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000, random_state=42)
)

LR.fit(X_train, Y_train)

LR_Pred = LR.predict(X_test)

LR_Accuracy = accuracy_score(Y_test, LR_Pred)

print("\n")
print("Logistic Regression Accuracy:", LR_Accuracy)


# Step 6: Train Decision Tree

DT = DecisionTreeClassifier(random_state=42)

DT.fit(X_train, Y_train)

DT_Pred = DT.predict(X_test)

DT_Accuracy = accuracy_score(Y_test, DT_Pred)

print("\n")
print("Decision Tree Accuracy:", DT_Accuracy)


# Step 7: Train KNN

KNN = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

KNN.fit(X_train, Y_train)

KNN_Pred = KNN.predict(X_test)

KNN_Accuracy = accuracy_score(Y_test, KNN_Pred)

print("\n")
print("KNN Accuracy:", KNN_Accuracy)


# Step 8: Individual Model Accuracy

print("\n")
print("Individual Model Accuracies")

print("Logistic Regression:", LR_Accuracy)
print("Decision Tree:", DT_Accuracy)
print("KNN:", KNN_Accuracy)


# Step 9: Create Hard Voting Classifier

Hard_Voting = VotingClassifier(
    estimators=[
        ("LR", LR),
        ("DT", DT),
        ("KNN", KNN)
    ],
    voting="hard"
)

Hard_Voting.fit(X_train, Y_train)

Hard_Pred = Hard_Voting.predict(X_test)

Hard_Accuracy = accuracy_score(Y_test, Hard_Pred)

print("\n")
print("Hard Voting Accuracy:", Hard_Accuracy)


# Step 10: Create Soft Voting Classifier

Soft_Voting = VotingClassifier(
    estimators=[
        ("LR", LR),
        ("DT", DT),
        ("KNN", KNN)
    ],
    voting="soft"
)

Soft_Voting.fit(X_train, Y_train)

Soft_Pred = Soft_Voting.predict(X_test)

Soft_Accuracy = accuracy_score(Y_test, Soft_Pred)

print("\n")

print("Soft Voting Accuracy:", Soft_Accuracy)


# Step 11: Compare All Models

Results = pd.DataFrame({
    "Model": [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Hard Voting",
        "Soft Voting"
    ],

    "Accuracy": [
        LR_Accuracy,
        DT_Accuracy,
        KNN_Accuracy,
        Hard_Accuracy,
        Soft_Accuracy
    ]
})

print("\n")

print("Final Model Comparison:")
print(Results.to_string(index=False))
