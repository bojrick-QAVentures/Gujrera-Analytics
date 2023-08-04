# data_quality_checks.py

import pandas as pd

def check_missing_values(dfs):
    # missing_values = {}
    # for key, df in dfs.items():
        # missing_values[key] = 
    missing_values = dfs.isnull().sum() / len(dfs) * 100
    return missing_values

def check_duplicates(dfs):
    # duplicates = {}
    # for key, df in dfs.items():
        # duplicates[key] = 
    duplicates = dfs.duplicated().sum()
    return duplicates

def check_constant_columns(df):
    # constant_columns = {}
    # for key, df in dfs.items():
        # constant_columns[key] = 
    constant_columns =   [col for col in df.columns if df[col].nunique() <= 1]
    return constant_columns

def summary_statistics(df):
    # summary_stats = {}
    # for key, df in dfs.items():
        # summary_stats[key] = 
    summary_stats = df.describe(include='all')
    return summary_stats
