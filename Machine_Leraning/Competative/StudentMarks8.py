# Plot a line chart of marks of 'Amit' across all subjects  

import pandas as pd
import matplotlib.pyplot as plt


def main():
    Subject = ["Math","Science","English"]
    Marks = [85,92,75]

    plt.plot(
        Subject,
        Marks,
        marker = "o",
        linestyle = "--",
        linewidth = 2,
        markersize = 7,
        label = "Marks"
    )

    plt.title("Amit_Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
