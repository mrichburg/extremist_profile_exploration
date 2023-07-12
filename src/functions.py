from string import ascii_letters
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import bokeh
import json
from pandas import json_normalize

#read csv or json into data frame fucntion
def read_file(file_path):
    """
    Read a file and return a DataFrame based on the file extension.

    Args:
        file_path (str): Path to the file.

    Returns:
        pandas.DataFrame: DataFrame containing the file data.
    """
    if file_path.endswith('.json'):
        with open(file_path) as f:
            d = json.load(f)
        return json_normalize(d['items'])
    elif file_path.endswith('.xlsx'):
        return pd.read_excel(file_path)
    else:
        print("Error: Invalid file extension.")
        return None

#example json_file_path = 'path/to/file.json'
#example json_df = read_file(json_file_path)


#return rows with confirmed US Military background

def mil_filter(df, start_year=None, end_year=None):
    """
    Filter DataFrame for only rows where value under Military column equals 1

    Args:
        df (pandas.Dataframe): DataFrame from which to pull filtered data
        start_year (int): First year in date range of filter
        end_year (int): Last year in date range of filter (inclusive)

    Returns:
        pandas.DataFrame: DataFrame containing only rows where value under Military column equals 1 within a given timeframe.
    """
    df = df[df['Military'] == 1]

    if start_year and end_year:
        return df[(df['Year_Exposure'] >= start_year) and (df['Year_Exposure'] <= end_year)]
    elif start_year and not end_year:
        return df[df['Year_Exposure'] >= start_year]
    elif end_year and not start_year:
        return df[df['Year_Exposure'] <= end_year]
    return df


"""


data cleaning
1 - Eliminated all duplicates
2 - Eliminate useless columns
    *Columns with all null values/ 88 values/ 99 values
"""

def clean(df):
    """
    Clean DataFrame of columns with all empty, null, N/A, or unknown values, and drops duplicate rows.

    Args:
        df (DataFrame): A DataFrame to be cleaned

    Returns: A DataFrame with useful data.
    """
    no_dups = df.drop_duplicates(subset="Subject_ID")



def unique_indicators(self):
    data_processor.read_csv()
    unique_indicators = self.data["Indicator Name"].unique()
    for indicator in unique_indicators:
        print(indicator)

for column in signals.columns:
if signals[column].isin(['', 'N/A']).all():
    signals = signals.drop(column, axis=1)



