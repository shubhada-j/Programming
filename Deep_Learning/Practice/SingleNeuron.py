import numpy as np

# Step 1 : Define input feaures ie X
#                 [x1,x2,x3]
input = np.array([2.0,3.0,4.0])
print("X : ",input)

# Step 2 : Define weights ie w
#                   [w1,w2,w3]
weights = np.array([0.5,0.3,0.2])
print("w : ",weights)


# Step 3 : Define bias ie b
#       b
bias = 1.0
print("b : ",bias)

# Step 4 : Calculate weighted sum ie Z
# z = x1w1 + x2w2 + x3w3 + b
# z = (2.0*5.0) + (3.0*3.0) + (4.0*2.0) + 1.0 
# dot -> method for multiplication
z = np.dot(input,weights) + bias
print("z : ",z)

# Step 5 : Acitivation Function (ReLU)
def ReLU(x):                                
    return max(0,x)                         

# Step 6 : Final Output
Y = ReLU(z)
print("Y : ",Y)
