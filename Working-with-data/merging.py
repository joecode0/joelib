import pandas as pd


def merge_to_compare_columns(df1, df2, merge_columns, compare_columns):
    """This function merges two dataframes by some common columns, and removes
    unwanted ones, so we can easily compare/ work with some select columns

    Args:
        df1 (pandas.DataFrame): First of two DataFrames that we merge
        df2 (pandas.DataFrame): Second of two DataFrames that we merge (order does not matter)
        merge_columns (String list): Header names for columns we want to merge on
        compare_columns (String list): Header names for columns we wish to compare

    Returns:
        df: Merged DataFrame with only the columns we want to compare, and the merging columns
    """

    df = df1.merge(df2, how='inner', on=merge_columns)
    new_cols = [x + "_x" for x in compare_columns]
    new_cols.extend([x + "_y" for x in compare_columns])
    new_cols.extend(merge_columns)

    remove_cols = [x for x in list(df.columns.values) if not x in new_cols]

    df.drop(remove_cols, axis=1, inplace=True)

    return df
