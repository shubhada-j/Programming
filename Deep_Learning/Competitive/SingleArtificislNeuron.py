import math

x1 = 2
x2 = 3
w1 = 0.4
w2 = 0.6
bias = 0.5

z = (x1 * w1) + (x2 * w2) + bias
print("Weighted Sum:", z)

output = 1 / (1 + math.exp(-z))
print("Final Output:", output)

if output > 0.5:
    print("Output is close to 1")
else:
    print("Output is close to 0")
