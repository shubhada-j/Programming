from PIL import Image

img = Image.open("digit.png")
print(img.size)                         # gives vertical and horizontal pixels count

img = img.convert("L")                  # converting into greyscale
img = img.resize((28,28))               # resizze the image

img.save("digit_28x28.png")

print(img.size)