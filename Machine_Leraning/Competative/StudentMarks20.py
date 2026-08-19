# Plot a boxplot for English marks to check disturibution and outliers

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    Data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(Data) 

    plt.boxplot(df['English'])

    plt.title("English Marks Distribution")
    plt.ylabel("English Marks")
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()