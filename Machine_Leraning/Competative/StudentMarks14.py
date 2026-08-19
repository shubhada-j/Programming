# Plot a pie chart of subject marks for 'Sagar'

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main(): 
    labels = ["Math", "Science", "English"]
    subject_marks = [90,88,85]
    
    plt.pie(
        subject_marks,
        labels=labels,
        radius = 1,
        autopct = "%1.1f%%",
        colors=["red","blue","green"]
    )

    plt.title("Sagar Marks")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()