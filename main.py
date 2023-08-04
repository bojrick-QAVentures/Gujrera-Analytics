from json_processing import process_json_files

# Define the keys to extract and their paths
keys = {
    'formThreeAList': ['projectExtra', 'getform-three-byid', 'data', 'formThreeAList'],
    'getProjectLocations': ['projectDetails', 'getProjectLocations'],
    'getproject-details': ['projectDetails', 'getproject-details', 'data'],
    'englist': ['projectDetails', 'getproject-details', 'data', 'englist'],
    'dev': ['projectDetails', 'getproject-details', 'data', 'dev'],
    'acrchlist': ['projectDetails', 'getproject-details', 'data', 'acrchlist'],
    'contr': ['projectDetails', 'getproject-details', 'data', 'contr'],
}

# TODO: Replace this with the list of your JSON files
json_files = ["file1.json", "file2.json", "file3.json"]

# Process the JSON files
dfs = process_json_files(json_files, keys)

# TODO: Handle the output (e.g., save the DataFrames to CSV files or load them into a database)
