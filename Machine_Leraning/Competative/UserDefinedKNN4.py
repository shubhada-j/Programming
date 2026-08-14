# Use KNN to predict whether a student passes or fails based on study hours and attendance

import math
import numpy as np

def MarvellousEucDistance(P1,P2):
    Ans = math.sqrt((P1['X']- P2['X'])**2 + (P1['Y']- P2['Y'])**2)
    return Ans

def MarvellousKNNClassifier(k = 5):
    Border = "-"*30

    Data = [
        {'Point' : 'A','X' : 2, 'Y' : 60, 'Label' : 'Fail'},
        {'Point' : 'B','X' : 5, 'Y' : 80, 'Label' : 'Pass'},
        {'Point' : 'C','X' : 6, 'Y' : 85, 'Label' : 'Pass'},
        {'Point' : 'D','X' : 1, 'Y' : 50, 'Label' : 'Fail'}
    ]

    print(Border)
    print("Marvellous KNN Classifier")
    print(Border)

    for i in Data:
        print(Data)

    print(Border)

    Study_hours = int(input("Enter the Study hours : "))
    Attendence = int(input("Enter the Attendence : "))

    new_point = {'X' : Study_hours, 'Y' : Attendence}

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
    print("Nearest 3 members are : ")
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