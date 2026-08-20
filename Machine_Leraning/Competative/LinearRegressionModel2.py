# Write a Python Program using Linear Regression to train a regiression model using a dataset below

import numpy as np 
from sklearn.linear_model import LinearRegression

def main():
    X = [1,2,3,4,5]
    Y = [7,6,7,6,8]
    Z = [50,55,60,65,70]

    Data = np.column_stack((X,Y))

    model = LinearRegression()

    model.fit(Data,Z)

    print("Coefficient of X : ", model.coef_[0])
    print("Coefficient of Y : ", model.coef_[1])
    print("Intercept : ", model.intercept_)

if __name__ == "__main__":
    main()