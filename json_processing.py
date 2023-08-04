import os
import json
import pandas as pd
from tqdm import tqdm
import concurrent.futures
import logging
import data_quality_checks  # import the data quality checks module

def process_json_file(json_file, keys):
    # Load the JSON data
    with open(json_file, "r") as file:
        json_data = json.load(file)

    # Initialize the dictionary of DataFrames
    dfs = {}

    # Process each key
    for key, path in keys.items():
        # Extract the data for this key
        data = json_data
        for p in path:
            data = data.get(p, {})

        # Create a DataFrame for this key
        if isinstance(data, list):
            dfs[key] = pd.json_normalize(data)
        elif isinstance(data, dict):
            dfs[key] = pd.json_normalize([data])
        else:
            dfs[key] = pd.DataFrame()

    return dfs

# from tqdm import tqdm
# # from concurrent.futures import ThreadPoolExecutor, as_completed
# import concurrent.futures as conf


def process_json_files(json_dir, keys,initial_dfs=None):
    """
    Process all JSON files in a directory and return a dictionary of DataFrames.

    Args:
    json_dir (str): The path to the directory with the JSON files.
    keys (dict): A dictionary of keys to extract from the JSON data.
    initial_dfs (dict): An optional dictionary of initial DataFrames to append to.

    Returns:
    dict: A dictionary of DataFrames.
    """
    # If no initial DataFrames are provided, start with an empty dictionary
    if initial_dfs is None:
        initial_dfs = {key: pd.DataFrame() for key in keys}

    # Get the list of JSON files in the directory
    json_files = [os.path.join(json_dir, file) for file in os.listdir(json_dir) if file.endswith('.json')]
    count = 0
    # Process each JSON file
    for json_file in tqdm(json_files, desc="Processing files"):
        # Process this JSON file
        dfs = process_json_file(json_file, keys)

    # Append the data to the initial DataFrames
    
        for key, df in dfs.items():
            initial_dfs[key] = pd.concat([initial_dfs[key], df], ignore_index=True)

    # Create a Pandas Excel writer using the 'xlsxwriter' engine
    # count +=1
    # if count%50==0:
        # try:
        #     file_stats = os.stat('Output\Guj-Rera Database 2022-December.xlsx')
        #     file_size = file_stats.st_size
        #     print(f"File Size in Bytes is {file_size}")
        # except FileNotFoundError:
        #     print("File not found.")
        # except OSError:
        #     print("OS error occurred.")


    #     # excel_writer = pd.ExcelWriter(f'Output/Guj-Rera Database 2022-December_{count}.xlsx', engine='xlsxwriter')
    #     for sheet_name, df in initial_dfs.items():
    #         df.to_excel('Output/Guj-Rera Database 2022-December_{count}.xlsx', sheet_name=sheet_name, index=False)

        # excel_writer.save()

    return initial_dfs