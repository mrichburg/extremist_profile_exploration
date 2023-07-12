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
    Filter DataFrame for only rows where value under Military column equals 1 and non-empty columns
    then turn it into a new excel file

    Args:
        df (pandas.Dataframe): DataFrame from which to pull filtered data
        start_year (int): First year in date range of filter
        end_year (int): Last year in date range of filter (inclusive)

    Returns:
        None
    """
    mil_only = df[df['Military'] == 1]
    needed_columns = mil_only[['Subject_ID', 'Year_Exposure', 'Radicalization_Islamist', 
                            'Radicalization_Far_Right', 'Radicalization_Far_Left',
                            'Radicalization_Single_Issue', 'Ideological_Sub_Category1', 
                            'Actively_Recruited', 'Internet_Radicalization', 'Media_Radicalization', 
                            'Social_Media', 'Social_Media_Platform1', 'Foreign_Govt_Leader', 
                            'US_Govt_Leader', 'Event_Influence1']]

    if start_year and end_year:
        result = needed_columns[(needed_columns['Year_Exposure'] >= start_year) and (needed_columns['Year_Exposure'] <= end_year)]
    elif start_year and not end_year:
        result = needed_columns[needed_columns['Year_Exposure'] >= start_year]
    elif end_year and not start_year:
        result = needed_columns[needed_columns['Year_Exposure'] <= end_year]
    else:
        result = needed_columns
    result.dropna(axis=1, how='all').to_excel("../data/PIRUS_March2023/final_mil.xlsx")

    return None

#Turning numbers in to words

def value_change(df, df_column_name, new_vals, new_column_name):
    """
    Create a copy of a DataFrame column but with human readable value. Drops column being copied.

    Args:
        df (pandas.Dataframe): DataFrame to make changes to
        df_column_name (str): Name of column to make a copy of
        new_vals (dict): Dictionary containing human readable values
        new_column_name(str): Name of the new column created

    Returns:
        None
    """
    df[new_column_name] = df[df_column_name].map(new_vals)
    df.drop(columns=[f"{df_column_name}"], inplace=True)

    return None

if __name__ == "__main__":
    pass
