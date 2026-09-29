sentence = "food was not good"

words = sentence.split()    #sentence split in tokens

for index, word in enumerate(words):        # enumerate -> ak ak value anun deto
    print("Position",index+1,":",word)
    