# Write a program that classifies a new data point using the k nearest neighbour algorithm 
# The algorithm should be implemented manually without using any machine learning library
# k = 1

import math
import numpy as np

def MarvellousEucDistance(P1,P2):
    Ans = math.sqrt((P1['X']- P2['X'])**2 + (P1['Y']- P2['Y'])**2)
    return Ans

def MarvellousKNNClassifier(k = 1):
    Border = "-"*30

    Data = [
        {'Point' : 'A','X' : 1, 'Y' : 2, 'Label' : 'Red'},
        {'Point' : 'B','X' : 2, 'Y' : 3, 'Label' : 'Red'},
        {'Point' : 'C','X' : 3, 'Y' : 1, 'Label' : 'Blue'},
        {'Point' : 'D','X' : 6, 'Y' : 5, 'Label' : 'Blue'}
    ]

    print(Border)
    print("Marvellous KNN Classifier")
    print(Border)

    for i in Data:
        print(Data)

    print(Border)

    new_point = { 'X' : 2, 'Y' : 2}

    print("Distances of all points : ")
    print(Border)

    for d in Data:
        d['distance'] = MarvellousEucDistance(d,new_point)

    for d in Data:
        print(d)

    print(Border)

    sorted_data = sorted(Data, key = lambda item : item['distance'])

    print(Border)
    print("sorted data : ")
    print(Border)

    for d in sorted_data:
        print(d)

    print(Border)

    nearest = sorted_data[:k]    # :k -> first 3 

    print(Border)
    print("Nearest member are : ")
    print(Border)

    for d in nearest:
        print(d)

    print(Border)

    # Voting
    votes = {}

    for neighboours in nearest:
        label = neighboours['Label']
        votes[label] = votes.get(label,0) + 1

    print(Border)
    print("Voting result is : ")
    print(Border)

    for d in votes:
        print("Name : ",d,"Number of votes : ",votes[d])

    print(Border)

    iMax = 0
    Name = ""

    for d in votes:
        if(votes[d] > iMax):
            iMax = votes[d]
            Name = d

    print("Final prediction is : ",Name)
    
    
def main ():
    MarvellousKNNClassifier()

if __name__ == "__main__":
    main()