# Using the regression model created in the previous question, write a python program to predict marks for 6 study hours and display the predicted value 

import numpy as np 
import pandas as pd

def main():
    X = [1,2,3,4,5]
    Y = [50,55,60,65,70]

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

    study_hours = 6

    predicted_marks = m * study_hours + c

    print("Study hours : ", study_hours)
    print("Predicted marks : ", predicted_marks)


if __name__ == "__main__":
    main()