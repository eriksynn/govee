
## first have to `pip install pandas` into python workspace


import pandas as pd
import numpy as np

def analyze_data():
    # Load the CSV file
    file_path = input("Please provide the input file name: ")

    if not file_path:  
        file_path = "C:\\Users\\eriks\\projects\\govee\\Start of 2024.csv"
    
    df = pd.read_csv(file_path)

    # Convert the timestamp column to datetime
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    df = df.round(1)

    for i in range(len(df.index)):
        if i == 0:
            df.at[i, "Peak"] = 0
            continue
        elif i == len(df.index) - 1:
            df.at[i, "Peak"] = 0
        else:
            curr_temp = df.at[i, "Temperature"]
            prev_temp = df.at[i-1, "Temperature"]
            next_temp = df.at[i+1, "Temperature"]
            if (curr_temp > (prev_temp + 0.2)):
                df.at[i, "Peak"] = 1
            else: 
                df.at[i, "Peak"] = 0

    peaks_per_day = df.groupby(df['Timestamp'].dt.date)['Peak'].apply(lambda x: len(x.loc[x == 1]))

    df.to_csv("C:\\Users\\eriks\\projects\\govee\\out.csv")
    peaks_per_day.to_csv("C:\\Users\\eriks\\projects\\govee\\ppd.csv")

    # Print the results
    print(peaks_per_day)
    print("Number of Days", len(peaks_per_day.index))
    print("Total number of peaks", df['Peak'].sum())


if __name__ == "__main__":
    analyze_data()
    print("done")

"""

    for temps in df["Temperature"].items():
        print(temps)

    conditions = [df['Temperature'].gt(df['Temperature'].shift(1)) &
                  df['Temperature'].gt(df['Temperature'].shift(1)) &
                  df['Temperature'].gt(df['Temperature'].shift(1))]
    categories = [1]
    df['Peak'] = np.select(conditions, categories, default=0)

    for i in range(len(df.index)):
        if i == 0:
            df.loc[i]["Peak"] = 0
            continue
        elif i == len(df.index) - 1:
            df.loc[i]["Peak"] = 0
        else:
            curr_temp = df.loc[i]["Temperature"]
            prev_temp = df.loc[i-1]["Temperature"]
            next_temp = df.loc[i+1]["Temperature"]
            if (curr_temp == prev_temp and curr_temp > next_temp):
                df.loc[i]["Peak"] = 1
                peaks_total += 1
"""