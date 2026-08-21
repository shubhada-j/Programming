# Train Linear regression model, Predict salary for 6 years of experience,Plot regression line using matplotlib

import matplotlib.pyplot as plt

def main():
    X = [1,2,3,4,5]
    Y = [20000,25000,30000,35000,40000]

    print("Experience : ",X)
    print("Salary : ",Y)
    
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

    experience = 6

    predicted_salary = m * experience + c

    print("Predicted salary for 6 years of experience : ",
          predicted_salary)

    # Plot regression line
    plt.scatter(X, Y, label="Actual Data")

    Y_pred = []

    for i in range(n):
        predicted_y = m * X[i] + c
        Y_pred.append(predicted_y)

    plt.plot(X, Y_pred, label="Regression Line")

    plt.scatter(experience, predicted_salary,
                label="Prediction for 6 Years")

    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()