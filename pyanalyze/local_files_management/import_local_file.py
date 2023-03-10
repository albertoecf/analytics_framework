import pandas as pd

def import_local_file_to_df(filepath):
    """
    This function imports data from a CSV or Excel file and loads it into a pandas DataFrame.

    Args:
        filepath (str): Path to the CSV or Excel file.

    Returns:
        pandas.DataFrame: DataFrame containing the data from the file.
    """
    if filepath.endswith('.csv'):
        df = pd.read_csv(filepath)
    elif filepath.endswith('.xls') or filepath.endswith('.xlsx'):
        df = pd.read_excel(filepath)
    else:
        raise ValueError('Invalid file format. Only CSV and Excel files are supported.')

    return df
