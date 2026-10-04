#Scattered Plot -> mostly use

import matplotlib.pyplot as plt

def main():
    study_hours = [1,2,3,4,5,6]
    marks = [35,42,50,62,72,85]

    plt.scatter(
        study_hours,
        marks,
        s = 100,
        marker="o",
        alpha=0.8,
        edgecolors="black",
        linewidths=1,
        label = "Students"
    )

    plt.title("Marvellous Scattered Plot")
    plt.xlabel("Study_hours")
    plt.ylabel("Obtained_Marks")
    plt.grid()                          #use in this type to read easily
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()