# Plot a line chart of marks of 'Amit' across all subjects  

import pandas as pd
import matplotlib.pyplot as plt


def main():
    Subject = ["Math","Science","English"]
    Marks = [85,92,75]

    plt.bar(
        Subject,
        Marks,
        width = 0.5,
        edgecolor = "black",
        linewidth = 1,
        alpha = 0.5,
        label = "Marks"
    )

    plt.title("Amit_Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()