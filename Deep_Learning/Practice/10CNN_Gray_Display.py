from PIL import Image
import numpy as np

img = Image.open("digit_28x28.png")
img = img.convert("L")
img = img.resize((28,28))

pixels = np.array(img)

print("Image Size : ",pixels.shape)         #shape : kiti by kiti

print("Pixel Values : ")
print(pixels)


# 0     Pure Black
# 255   Pure White
# 50    Dark Gray
# 120   Medium Gray
# 200   Light Gray

#C:\Users\mdman\Desktop\Python\Deep_Learning>python 10CNN_Gray_Display.py > output.txt