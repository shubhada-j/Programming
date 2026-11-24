import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.metrics import classification_report

# Step 1: Create Dataset

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

y = np.array([
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
])

print("Dataset Loaded Successfully")

print("X Shape:", X.shape)
print("Y Shape:", y.shape)


# Step 2: Clean Dataset

print("\nMissing Values:", np.isnan(X).sum())

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


# Step 11: Test New Customer

new_customer = np.array([
    [46, 1450, 5, 6, 9]
])
new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)

if prediction[0] == 0:
    print("\nPrediction: Customer will stay")
else:
    print("\nPrediction: Customer may leave")
