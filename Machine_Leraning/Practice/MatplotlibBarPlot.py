#Bar Plot

import matplotlib.pyplot as plt

def main():
    language = ["C","C++","Java","Python"]
    students = [30,40,35,55]

    plt.bar(
        language,                   # value of x-axis
        students,                   # value of y-axis
        width = 0.6,                # width of bars
        edgecolor = "black",        # boarder color od bars
        linewidth = 1,              # width of bar border
        alpha = 0.8,                # transperance 0.0 to 1.0
        label = "Students"          # legend text

    )


    plt.title("Marvellous Bar Plot")
    plt.xlabel("Languages")
    plt.ylabel("Number of students")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
