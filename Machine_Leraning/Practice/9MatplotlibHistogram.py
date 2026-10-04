#Histogram -> mostly use

import matplotlib.pyplot as plt

def main():
    marks = [45,55,60,62,65,67,70,72,75,78,80,82,85,90,92]

    plt.hist(
        marks,              # continuous data
        bins=5,             # number of groups
        edgecolor="Black",  # border color
        alpha=0.8,          # transperency
        rwidth=0.9          # realtive width of bars
    )   

    plt.title("Marvellous Histogram")
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.show()

if __name__ == "__main__":
    main()