
# ============================================================
# LOAN DEFAULT PREDICTION USING MULTI-LAYER PERCEPTRON (MLP)
# ============================================================

# STEP 1: IMPORT REQUIRED LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

import warnings
warnings.filterwarnings("ignore")

# STEP 2: LOAD AND UNDERSTAND DATASET

df = pd.read_csv("Loan_Default (1).csv")

print("\n========== DATASET ==========")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Information:")
print(df.info())

print("\nStatistical Description:")
print(df.describe())

# STEP 3: FIND MISSING VALUES

print("\n========== MISSING VALUES ==========")

print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# STEP 4: CHECK DUPLICATE VALUES

print("\nDuplicate Records:")
print(df.duplicated().sum())

# STEP 5: EXPLORATORY DATA ANALYSIS

# Target variable distribution

print("\n========== TARGET DISTRIBUTION ==========")

print(df["Default"].value_counts())

print("\nTarget Percentage:")
print(df["Default"].value_counts(normalize=True) * 100)

# Visualize target distribution

sns.countplot(x="Default", data=df)

plt.title("Loan Default Distribution")
plt.xlabel("Default")
plt.ylabel("Number of Applicants")
plt.show()

# Numerical feature distribution

df.hist(figsize=(15, 10))

plt.suptitle("Numerical Feature Distribution")
plt.tight_layout()
plt.show()

# Correlation heatmap (numerical features only)

plt.figure(figsize=(12, 8))

sns.heatmap(
    df.select_dtypes(include=np.number).corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

# STEP 6: ENCODE CATEGORICAL VARIABLES

print("\n========== ENCODING ==========")

df = pd.get_dummies(
    df,
    columns=["PreviousDefault", "HomeOwnership"],
    drop_first=True,
    dtype=int
)

print(df.head())

print("\nEncoded Columns:")
print(df.columns)

# STEP 7: SEPARATE X AND Y

X = df.drop("Default", axis=1)

y = df["Default"]

print("\nX Shape:", X.shape)
print("Y Shape:", y.shape)

# STEP 8: TRAIN-TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n========== TRAIN TEST SPLIT ==========")

print("X Train:", X_train.shape)
print("X Test:", X_test.shape)

print("Y Train:", y_train.shape)
print("Y Test:", y_test.shape)

# Check class distribution after stratified splitting

print("\nTraining Class Distribution:")
print(y_train.value_counts(normalize=True))

print("\nTesting Class Distribution:")
print(y_test.value_counts(normalize=True))

# STEP 9: FEATURE SCALING

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)

print("\nFeature Scaling Completed!")

# STEP 10: CREATE MLP CLASSIFIER

model = MLPClassifier(

    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print("\n========== MLP MODEL ==========")

print(model)

# STEP 11: TRAIN THE MODEL

model.fit(X_train, y_train)
print("\nModel Training Completed!")

# STEP 12: MAKE PREDICTIONS

y_pred = model.predict(X_test)
print("\n========== PREDICTIONS ==========")
print("Actual Values:")
print(y_test.values)
print("\nPredicted Values:")
print(y_pred)

# STEP 13: CALCULATE ACCURACY

accuracy = accuracy_score(y_test, y_pred)
print("\n========== MODEL ACCURACY ==========")
print("Accuracy:", accuracy * 100, "%")

# STEP 14: GENERATE CONFUSION MATRIX

cm = confusion_matrix(y_test, y_pred)
print("\n========== CONFUSION MATRIX ==========")
print(cm)
plt.figure(figsize=(6, 4))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.xlabel("Predicted Values")
plt.ylabel("Actual Values")
plt.title("Confusion Matrix")
plt.show()

# STEP 15: GENERATE CLASSIFICATION REPORT

print("\n========== CLASSIFICATION REPORT ==========")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))

# STEP 16: CALCULATE PRECISION, RECALL AND F1 SCORE

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

print("\n========== PERFORMANCE METRICS ==========")
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)

# STEP 17: PLOT TRAINING LOSS

plt.figure(figsize=(8, 5))
plt.plot(model.loss_curve_)
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("MLP Training Loss Curve")
plt.show()

# ============================================================
# HYPERPARAMETER EXPERIMENTS
# ============================================================

# EXPERIMENT 1: ACTIVATION FUNCTIONS

print("\n========== EXPERIMENT 1: ACTIVATION ==========")

activations = [
    "identity",
    "logistic",
    "tanh",
    "relu"
]

activation_results = []

for activation in activations:
    clf = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation=activation,
        solver="adam",
        max_iter=1000,
        random_state=42

    )

    clf.fit(X_train, y_train)

    prediction = clf.predict(X_test)

    acc = accuracy_score(y_test, prediction)

    prec = precision_score(
        y_test, prediction, zero_division=0
    )

    rec = recall_score(
        y_test, prediction, zero_division=0
    )

    f1_value = f1_score(
        y_test, prediction, zero_division=0
    )

    activation_results.append([
        activation, acc, prec, rec, f1_value
    ])

    print(
        activation,
        "Accuracy:",
        acc * 100
    )

activation_df = pd.DataFrame(
    activation_results,
    columns=[
        "Activation",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
)

print("\nActivation Experiment Results:")
print(activation_df)

# EXPERIMENT 2: HIDDEN LAYERS

print("\n========== EXPERIMENT 2: HIDDEN LAYERS ==========")

layers = [
    (10,),
    (20, 10),
    (50, 25),
    (100, 50, 25)
]

layer_results = []

for layer in layers:
    clf = MLPClassifier(
        hidden_layer_sizes=layer,
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42

    )

    clf.fit(X_train, y_train)

    prediction = clf.predict(X_test)

    acc = accuracy_score(y_test, prediction)

    prec = precision_score(
        y_test, prediction, zero_division=0
    )

    rec = recall_score(
        y_test, prediction, zero_division=0
    )

    f1_value = f1_score(
        y_test, prediction, zero_division=0
    )

    layer_results.append([
        str(layer), acc, prec, rec, f1_value
    ])

    print(
        layer,
        "Accuracy:",
        acc * 100
    )


layer_df = pd.DataFrame(
    layer_results,
    columns=[
        "Hidden Layers",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
)

print("\nHidden Layer Experiment Results:")
print(layer_df)

# EXPERIMENT 3: LEARNING RATE

print("\n========== EXPERIMENT 3: LEARNING RATE ==========")

learning_rates = [
    0.0001,
    0.001,
    0.01
]

learning_results = []

for rate in learning_rates:
    clf = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        learning_rate_init=rate,
        max_iter=1000,
        random_state=42

    )

    clf.fit(X_train, y_train)

    prediction = clf.predict(X_test)

    acc = accuracy_score(y_test, prediction)

    prec = precision_score(
        y_test, prediction, zero_division=0
    )

    rec = recall_score(
        y_test, prediction, zero_division=0
    )

    f1_value = f1_score(
        y_test, prediction, zero_division=0
    )

    learning_results.append([
        rate, acc, prec, rec, f1_value
    ])

    print(
        rate,
        "Accuracy:",
        acc * 100
    )

learning_df = pd.DataFrame(
    learning_results,
    columns=[
        "Learning Rate",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
)

print("\nLearning Rate Experiment Results:")
print(learning_df)

# ============================================================
# TEST NEW LOAN APPLICANTS
# ============================================================

print("\n========== NEW LOAN APPLICANTS ==========")

new_applicant = pd.DataFrame({
    "Age": [30, 45],
    "Income": [600000, 900000],
    "LoanAmount": [300000, 500000],
    "CreditScore": [720, 650],
    "EmploymentYears": [5, 15],
    "ExistingLoans": [1, 3],
    "MonthlyDebt": [10000, 25000],
    "LoanTerm": [36, 60],
    "PreviousDefault": ["No", "Yes"],
    "HomeOwnership": ["Own", "Rent"]

})

# Encode new applicant data using the same categories

new_applicant = pd.get_dummies(
    new_applicant,
    columns=["PreviousDefault", "HomeOwnership"],
    drop_first=True,
    dtype=int

)

# Match the training feature columns

new_applicant = new_applicant.reindex(
    columns=X.columns,
    fill_value=0
)

# Scale new applicant data

new_applicant_scaled = scaler.transform(new_applicant)

# Predict loan default risk

new_predictions = model.predict(new_applicant_scaled)

for i, prediction in enumerate(new_predictions):
    if prediction == 0:
        print(
            "Applicant",
            i + 1,
            ": Low Default Risk"
        )
    else:
        print(
            "Applicant",
            i + 1,
            ": High Default Risk"
        )

# ============================================================
# FINAL CONCLUSION
# ============================================================

print("\n========== FINAL CONCLUSION ==========")
print("Loan Default Prediction using MLP Completed!")
print("Model Accuracy:", accuracy * 100, "%")
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("\nAll Three Hyperparameter Experiments Completed!")
