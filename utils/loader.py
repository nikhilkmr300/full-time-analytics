import pandas as pd

def clean_data(data):
    data.columns = [column_name.lower().strip().replace(" ", "_") for column_name in data.columns]
    return data

def load_data(filepath):
    data = pd.read_csv(filepath, sep="\t")
    data = clean_data(data)
    return data
