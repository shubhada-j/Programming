#-------------------------------------------------------------
#  Deep Learning Pipeline
#-------------------------------------------------------------
# 1. Read the data from CSV     
# 2. Data Analysis (EDA)
# 3. Preprocessing
# 4. Train the Split
# 5. Feature Scaling
# 6. FNN  model training
# 7. Model Evaluation
# 8. Graphivcal Representation
# 9. Model Preserve
# 10. Model loading and preserve
# 11. Test unseen data
#-------------------------------------------------------------


#-------------------------------------------------------------
# Importing required libraries
#-------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

#-------------------------------------------------------------
# 1. Read the data from CSV   
#-------------------------------------------------------------

print("1. Read the data from CSV")

data = pd.read_csv("placement_data.csv")

print("Complete Dataset : ")
print(data)

#-------------------------------------------------------------
# 2. Data Analysis (EDA)
#-------------------------------------------------------------

print("2. Data Analysis (EDA)")

print("First 5 rows : ")
print(data.head())

print("COlumns name : ")
print(data.columns)

print("Shape of Dataset : ")
print(data.shape)

print("Statistical Summary :")
print(data.describe)

#-------------------------------------------------------------
# 3. Preprocessing 
#-------------------------------------------------------------

print(" 3. Preprocessing")

X = data[['Aptitude','Coding','Communication','Academics','Internship']]
Y = data['Placed']

print("Input Features : ")
print(X.head())

print("Target : ")
print(Y.head())

#-------------------------------------------------------------
# 4. Train the Split
#-------------------------------------------------------------

print("4. Train the Split")

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.30,random_state=42)

print("Training Input Shape : ",X_train.shape)
print("Testing Input SHape : ",X_test.shape)
print("Training Output SHape : ",Y_train.shape)
print("Testing Output SHape : ",Y_test.shape)

#-------------------------------------------------------------
# 5. Feature Scaling
#-------------------------------------------------------------

print("5. Feature Scaling")

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.fit_transform(X_test)

print("Scaled training data : ")
print(X_train_scaled[:5])

#-------------------------------------------------------------
# 6. FNN  model training
#-------------------------------------------------------------

print("6. FNN  model training")

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver="adam",
    max_iter=1000,
    random_state=42
)

print(model)

print("Train the model")

model.fit(X_train_scaled,Y_train)

print("Model training completed")

#-------------------------------------------------------------
# 7. Model Evaluation
#-------------------------------------------------------------

print(" 7. Model Evaluation")

Y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy is : ",accuracy)

cm = confusion_matrix(Y_test,Y_pred)

print("Confusion Matrix : ",cm)

print("Predict the probablity")

Y_prob = model.predict_proba(X_test_scaled)

print(Y_prob[:5])

#-------------------------------------------------------------
# 8. Graphivcal Representation
#-------------------------------------------------------------

#-------------------------------------------------------------
# 9. Model Preserve
#-------------------------------------------------------------

#dump ne data harddisk var jato
print("9. Model Preserve")

joblib.dump(model,"placement_fnn_model.pkl")
joblib.dump(scalar,"placement_fnn_scalar.pkl")

print("Model and Scalar gets dump successfully")

#-------------------------------------------------------------
# 10. Model loading and preserve
#-------------------------------------------------------------
print("10. Model loading and preserve")

loaded_model = joblib.load("placement_fnn_model.pkl")
loaded_scalar = joblib.load("placement_fnn_scalar.pkl")

print("Model gets loaded successfully")

#-------------------------------------------------------------
# 11. Test unseen data
#-------------------------------------------------------------
# Aptitude :        70
# Coding :          75
# Communication :   80 
# Academics :       85
# Internship :      1
#-------------------------------------------------------------
print("11. Test unseen data")

#1:1 mapping to read
new_student = pd.DataFrame([[70,75,80,85,1]], columns=['Aptitude','Coding','Communication','Academics','Internship'])

new_student_scaled = loaded_scalar.transform(new_student)

new_prediction = loaded_model.predict(new_student_scaled)

new_probablity = loaded_model.predict_proba(new_student_scaled)

print("New Student Data : ")
print(new_student)

print("Prediction Probablity : ",new_probablity)

if new_prediction[0] == 1:
    print("Prediction : Placed")
else:
    print("Prediction : Not placed")