#Line Plot

import matplotlib.pyplot as plt

def main():
    X = [1,2,3,4,5]             #imagine its X-axis
    Y = [10,25,18,35,30]

    plt.plot(
        #positional parameter (sequence imp)
        X,                                      # values of x axis
        Y,                                      # values of y axis
        #keyword(not sequence mandatory)
        marker = "o",
        linestyle = "--",
        linewidth = 2,
        markersize = 7,
        label = "Marks"
    )

    plt.title("Marvellous Line Plot")
    plt.xlabel("Student Number")
    plt.ylabel("Marks")

    plt.grid(True)

    plt.legend()            #use to display all names

    plt.show()              # for diagram

if __name__ == "__main__":
    main()