# Create a bar plot of student name vs total marks 

import pandas as pd
import matplotlib.pyplot as plt


def main():
    Name = ["Amit","Sagar","Pooja"]
    Total = [252,258,240] 

    plt.bar(
        Name,
        Total,
        width = 0.5,
        edgecolor = "black",
        linewidth = 1,
        alpha = 0.5,
        label = "Total_Marks"
    )

    plt.title("Student_Marks")
    plt.xlabel("Student_Name")
    plt.ylabel("Total_Marks")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()