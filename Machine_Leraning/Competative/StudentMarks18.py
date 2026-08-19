# Export the final DataFrame to a CSV file

import pandas as pd
import numpy as np


def main():
    Data = {
        'Name' : ['Amit','Sagar','Pooja'],
        'Math' : [85,90,78],
        'Science' : [92,88,80],
        'English' : [75,85,82]
    }

    df = pd.DataFrame(Data) 

    min_value = df['Math'].min()
    max_value = df['Math'].max()

    df['math_normalized_value'] = (df['Math'] - min_value) / (max_value - min_value)

    df['Gender'] = ['M','M','F']

    result = df.groupby('Gender')[['Math','Science','English']].mean()
   
    df = pd.get_dummies(df,columns=['Gender'])

    df['Total'] = df['Math'] + df['Science'] + df['English']
    
    df['Status'] = df['Total'].apply(
            lambda total : 'Pass' if total >= 250 else 'Fail'
    )

    # save the dataframe into csv file
    df.to_csv('Output_File.csv',index_label=False)

if __name__ == "__main__":
    main()