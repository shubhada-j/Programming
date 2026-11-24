import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

# Step 1: Load Dataset

df = pd.read_csv("Fraudulent_Transaction_Detection (1).csv")

print("Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)


# Step 2: Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())


# Step 3: Separate Input and Output Variables

X = df.drop("Fraud", axis=1)

Y = df["Fraud"]


# Step 4: Split Training and Testing Data

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42,
    stratify=Y
)


# Step 5: Create Decision Tree Classifier

DT = DecisionTreeClassifier(random_state=42)

DT.fit(X_train, Y_train)


# Step 6: Create Bagging Classifier

BG = BaggingClassifier(
    n_estimators=50,
    random_state=42
)

BG.fit(X_train, Y_train)


# Step 7: Create Random Forest Classifier

RF = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    class_weight="balanced"
)

RF.fit(X_train, Y_train)


# Step 8: Create AdaBoost Classifier

AB = AdaBoostClassifier(
    n_estimators=50,
    learning_rate=0.5,
    random_state=42
)

AB.fit(X_train, Y_train)


# Step 9: Create Voting Classifier

VC = VotingClassifier(
    estimators=[
        ("DT", DT),
        ("RF", RF),
        ("AB", AB)
    ],
    voting="soft"
)

VC.fit(X_train, Y_train)


# Step 10: Calculate Evaluation Metrics

Models = {
    "Decision Tree": DT,
    "Bagging": BG,
    "Random Forest": RF,
    "AdaBoost": AB,
    "Voting": VC
}

Results = []

for Name, Model in Models.items():

    Prediction = Model.predict(X_test)

    Accuracy = accuracy_score(Y_test, Prediction)

    Precision = precision_score(
        Y_test, Prediction, zero_division=0
    )

    Recall = recall_score(
        Y_test, Prediction, zero_division=0
    )

    F1 = f1_score(
        Y_test, Prediction, zero_division=0
    )

    CM = confusion_matrix(
        Y_test, Prediction, labels=[0, 1]
    )

    Results.append({
        "Algorithm": Name,
        "Accuracy": Accuracy,
        "Precision": Precision,
        "Recall": Recall,
        "F1": F1
    })

    print("\n", Name)
    print("-----------------------")

    print("Accuracy:", Accuracy)
    print("Precision:", Precision)
    print("Recall:", Recall)
    print("F1 Score:", F1)

    print("Confusion Matrix:")
    print(CM)


# Step 11: Final Comparison

Final_Results = pd.DataFrame(Results)

print("\nFinal Model Comparison:")

print(Final_Results.to_string(index=False))
