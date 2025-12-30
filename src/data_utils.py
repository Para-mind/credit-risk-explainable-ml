import pandas as pd
from pathlib import Path

DATA_Dir = Path(__file__).resolve().parents[1] / "data"

def load_raw_data(file_name = "credit_risk_dataset.csv"):
    """
    Load the raw credit risk dataset from the data directory.

    Parameters:
    file_name (str): The name of the CSV file to load.

    Returns:
    pd.DataFrame: The loaded dataset as a pandas DataFrame.
    """
    file_path = DATA_Dir /"raw"/file_name
    return pd.read_csv(file_path)


def load_cleaned_data(file_name = "credit_risk_dataset_cleaned.csv"):
    """
    Load the cleaned credit risk dataset from the data directory.

    Parameters:
    file_name (str): The name of the CSV file to load.

    Returns:
    pd.DataFrame: The loaded cleaned dataset as a pandas DataFrame.
    """
    file_path = DATA_Dir / "processed" / file_name
    return pd.read_csv(file_path)