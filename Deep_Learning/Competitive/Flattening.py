matrix = [
    [6, 4],
    [8, 6]
]

# Step 1: Flatten the matrix

flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("Input Matrix:")

for row in matrix:
    print(row)

print()

print("Flatten Output:")
print(flatten_output)

# Step 2: Fully Connected Layer

weights = [1, 2, 1, 2]
bias = 1

result = 0

for i in range(4):
    result = result + (flatten_output[i] * weights[i])

result = result + bias

print()

print("Fully Connected Calculation:")
print("Output =", result)