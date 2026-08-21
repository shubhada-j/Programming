# Caluclate model performance 
# Predict all Y values using regression equation
# Calculate : MSE , R2 score

import numpy as np 
import pandas as pd

def main():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Study hours are : ",X)
    print("Values of Marks hours are : ",Y)

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print("Mean_X is : ",mean_x)
    print("Mean_Y is : ",mean_y)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x)**2) 

    m = numerator / denominator

    print("Slope of line is m : ",m)

    c = mean_y - m * mean_x

    print("Y intercept that is C : ",c)

    print("Regression Equation : ", "Y = " ,m,"X +",c )

    Y_pred = []

    for i in range(n):
        prediction_y = m * X[i] + c
        Y_pred.append(prediction_y)

    print("Actual Values of Y : ", Y)
    print("Predicted Y Values : ", Y_pred)

    mse_sum = 0

    for i in range(n):
        mse_sum = mse_sum + (Y[i] - Y_pred[i]) ** 2

    mse = mse_sum / n

    print("Mean Square Error : ",mse)

    ss_res = 0
    ss_tot = 0

    for i in range(n):
        ss_res = ss_res + (Y[i] - Y_pred[i]) ** 2
        ss_tot = ss_tot + (Y[i] - mean_y) ** 2

    r2 = 1 - (ss_res / ss_tot)

    print("R2 score : ",r2)

if __name__ == "__main__":
    main()