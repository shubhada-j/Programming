image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

feature_map = []

for i in range(3):
    row = []
    for j in range(3):
        region = [
            image[i][j:j+3],
            image[i+1][j:j+3],
            image[i+2][j:j+3]
        ]

        print("Region")
        
        for r in region:
            print(r)

        print("-"*30)

        print("Kernel")
        
        for r in kernel:
            print(r)
        
        print("-"*30)

        result = 0

        print("Calculation:")

        for x in range(3):
            for y in range(3):
                multiplication = region[x][y] * kernel[x][y]

                print(
                    str(region[x][y]) + "*" +
                    str(kernel[x][y]),
                    end=" "
                )

                result = result + multiplication

        print() 

        print("-"*30)

        print("Output =", result)

        print("-"*30)

        row.append(result)

    feature_map.append(row)
    print("-"*30)

print("Final Feature Map:")

for row in feature_map:
    print(row)

print("-"*30)