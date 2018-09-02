import pandas as pd
import numpy as np

# TODO: Some sort of top analysis function for database type data
# TODO: Some sort of top analysis function for timeseries type data
# TODO: etc.


def return_value_ranges(df_data, value_columns, many_duplicates=False):
    ranges_dict = dict()

    for col in list(df_data.columns.values):
        col_list = df_data[col].tolist()
        col_min = min(col_list)
        col_max = max(col_list)
        ranges_dict[col] = [col_min, col_max]

    return ranges_dict
