import pandas as pd

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def main():
    Border = "-" * 40

    # Step 1 : Load the Dataset

    print(Border)
    print("Step 1 : Load the Dataset")
    print(Border)

    df = pd.read_csv("breast_cancer.csv")

    print("Data Loaded Successfully")

    print("First few Entries : ")
    print(df.head())

    # Step 2 : Data Analysis (EDA)

    print(Border)
    print("Step 2 : Data Analysis (EDA)")
    print(Border)

    print("Shape of Dataset : ", df.shape)

    print("Column names : ", list(df.columns))

    print("Missing values per column : ")
    print(df.isnull().sum())

    print("Statistical report : ")
    print(df.describe())

    # Step 3 : Prepare Dataset

    print(Border)
    print("Step 3 : Prepare Dataset")
    print(Border)

    X = df.drop("target", axis=1)
    Y = df["target"]

    # Remove ID column if present
    if "id" in X.columns:
        X = X.drop("id", axis=1)

    print("Shape of X : ", X.shape)
    print("Shape of Y : ", Y.shape)

    # Step 4 : Split Dataset

    print(Border)
    print("Step 4 : Split Dataset")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("Details of Training and Testing Data")
    print(Border)

    print("Shape of X_train : ", X_train.shape)
    print("Shape of X_test : ", X_test.shape)
    print("Shape of Y_train : ", Y_train.shape)
    print("Shape of Y_test : ", Y_test.shape)

    # Step 5 : Feature Scaling

    print(Border)
    print("Step 5 : Feature Scaling")
    print(Border)

    scalar = StandardScaler()

    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.transform(X_test)

    print("Feature Scaling Completed")

    # Step 6 : Calculate Accuracy

    print(Border)
    print("Step 6 : Calculate Accuracy")
    print(Border)

    accuracy_scores = []

    K_values = range(1, 21)

    for k in K_values:

        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train_scaled, Y_train)

        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test, Y_pred)

        accuracy_scores.append(accuracy)

        print("K =", k, "Accuracy =", accuracy)

    print(Border)
    print("Accuracy Report")
    print(Border)

    for i in range(len(K_values)):
        print("K =", K_values[i], "Accuracy =", accuracy_scores[i])

    # Find Best K

    best_accuracy = max(accuracy_scores)

    best_k = K_values[accuracy_scores.index(best_accuracy)]

    print(Border)
    print("Best K : ", best_k)
    print("Best Accuracy : ", best_accuracy)

    # Step 7 : Final Model

    print(Border)
    print("Step 7 : Final Model")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=best_k)

    model.fit(X_train_scaled, Y_train)

    Y_pred = model.predict(X_test_scaled)

    # Step 8 : Confusion Matrix

    print(Border)
    print("Step 8 : Confusion Matrix")
    print(Border)

    print(confusion_matrix(Y_test, Y_pred))

    # Step 9 : Classification Report

    print(Border)
    print("Step 9 : Classification Report")
    print(Border)

    print(classification_report(Y_test, Y_pred))


if __name__ == "__main__":
    main()
