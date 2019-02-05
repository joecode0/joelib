import pandas as pd
import numpy as np

# TODO: Some sort of top analysis function for database type data
# TODO: Heatmap of coorelations between all columns pairwise
# TODO: Create nice plot for investigating correlation between 2 columns:
# i.e scatter plot
# best fit line
# correlation value in title
# extrapolation?


def return_value_ranges(df_data, value_columns):
    ranges_dict = dict()

    for col in list(df_data.columns.values):
        col_list = df_data[col].tolist()
        col_min = min(col_list)
        col_max = max(col_list)
        ranges_dict[col] = [col_min, col_max]

    return ranges_dict
