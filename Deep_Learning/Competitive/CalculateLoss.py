import numpy as np

actual = np.array([1, 0, 1, 1])

predicted = np.array([0.9, 0.2, 0.7, 0.4])

mse = np.mean((actual - predicted) ** 2)

print("Mean Squared Error:", mse)

epsilon = 1e-15

predicted = np.clip(predicted, epsilon, 1 - epsilon)

bce = -np.mean(
    actual * np.log(predicted) +
    (1 - actual) * np.log(1 - predicted)
)

print("Binary Cross Entropy:", bce)
print("\nMSE is used for Regression.")
print("Binary Cross Entropy is used for Classification.")
