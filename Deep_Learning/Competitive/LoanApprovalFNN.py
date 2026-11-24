import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report

# Step 1: Create Dataset

X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 10000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
])

y = np.array([
    0, 1, 1, 0, 1,
    1, 0, 1, 0, 1
])

print("Dataset Loaded Successfully")
print("X Shape:", X.shape)
print("Y Shape:", y.shape)


# Step 2: Preprocess Categorical Values

# Employment Status is already encoded:
# 0 = Not Stable
# 1 = Stable

print("\nEmployment Status is already encoded.")

# Step 3: Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)


# Step 4: Apply StandardScaler

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)

X_test = scaler.transform(X_test)


# Step 5: Create FNN Model

model = MLPClassifier(
    hidden_layer_sizes=(8, 4),
    activation="relu",
    solver="adam",
    max_iter=2000,
    random_state=42
)

# Step 6: Train Model

model.fit(X_train, y_train)

print("\nModel Training Completed!")

# Step 7: Predict Test Data

y_pred = model.predict(X_test)

print("\nActual Values:")
print(y_test)

print("\nPredicted Values:")
print(y_pred)

# Step 8: Evaluate Accuracy

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:", accuracy * 100, "%")

# Step 9: Confusion Matrix

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Step 10: Classification Report

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

# Step 11: Test New Applicant

new_applicant = np.array([
    [55000, 720, 400000, 10000, 1]
])

new_applicant_scaled = scaler.transform(new_applicant)

prediction = model.predict(new_applicant_scaled)

if prediction[0] == 0:
    print("\nPrediction: Loan Rejected")
else:
    print("\nPrediction: Loan Approved")
