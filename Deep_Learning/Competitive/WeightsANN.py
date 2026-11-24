import math

x = float(input("Enter input: "))
weight = float(input("Enter weight: "))
bias = float(input("Enter bias: "))
target = float(input("Enter target output: "))
learning_rate = float(input("Enter learning rate: "))

old_weight = weight
z = (x * weight) + bias
prediction = 1 / (1 + math.exp(-z))
print("\nPrediction:", prediction)

error = target - prediction
print("Error:", error)

gradient = (prediction - target) * prediction * (1 - prediction) * x
weight = weight - (learning_rate * gradient)
bias = bias - (learning_rate * (prediction - target) * prediction * (1 - prediction))

print("\nOld Weight:", old_weight)
print("Updated Weight:", weight)
print("Updated Bias:", bias)
