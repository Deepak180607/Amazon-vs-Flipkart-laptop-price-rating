import pandas as pd

def clean_data(df):

    df.drop_duplicates(inplace=True)

    df["value_score"] = df["Ratings"] / df["Price"]

    df_sorted = df.sort_values(by="value_score", ascending=False)

    print("Cleaned data saved!")
    return df_sorted
