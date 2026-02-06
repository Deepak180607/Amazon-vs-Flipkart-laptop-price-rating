import pandas as pd
def clean_data(df):
    df.drop_duplicates(inplace=True)
    df["value_score"] = df["Ratings"]/df["Prices"]
    df_sorted = df.sort_values(by = "value_score", ascending=False)
    print("Cleaned Data")
    return df_sorted
