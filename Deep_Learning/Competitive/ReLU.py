feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

# Step 1: Apply ReLU

relu = []

for row in feature_map:

    new_row = []

    for value in row:

        if value < 0:
            new_row.append(0)
        else:
            new_row.append(value)

    relu.append(new_row)


print("Feature Map:")
for row in feature_map:
    print(row)

print()

print("After ReLU:")
for row in relu:
    print(row)


# Step 2: Apply 2x2 Max Pooling

pool_size = 2

max_pool = []

for i in range(0, len(relu) - 1, 2):

    row = []

    for j in range(0, len(relu[0]) - 1, 2):

        max_value = max(
            relu[i][j],
            relu[i][j+1],
            relu[i+1][j],
            relu[i+1][j+1]
        )

        row.append(max_value)

    max_pool.append(row)

print()

print("After 2x2 Max Pooling:")
for row in max_pool:
    print(row)