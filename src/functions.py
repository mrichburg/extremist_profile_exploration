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
