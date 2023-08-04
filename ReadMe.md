# GujRera Data Pipeline

## Introduction

Welcome to the GujRera Data Pipeline project. This project is an end-to-end Extract, Transform, and Load (ETL) pipeline designed to fetch and process data from the [GujRera website](https://gujrera.gujarat.gov.in/). The pipeline transforms the data into a format that's convenient for analysis, thereby serving as a valuable resource for data scientists, analysts, real estate enthusiasts, government entities, corporations, and students.

## Project Overview

The pipeline deals with a complex JSON structure and flattens it into a more analysis-friendly format. The extracted data is stored in various tables, each representing a different aspect of a real estate project. The pipeline is designed to handle large volumes of data and can process multiple JSON files in an efficient manner.

## Features

1. **Robust Data Extraction:** Our pipeline navigates through the nested JSON structures from the [GujRera website](https://gujrera.gujarat.gov.in/) and extracts pertinent information.
2. **Data Transformation:** The pipeline transforms complex and nested JSON data into a tabular format, making it ready for analysis.
3. **Scalability:** The pipeline is designed to handle multiple JSON files, making it easy to append new data every quarter.
4. **Ease of Use:** With clear documentation and well-commented code, the pipeline is user-friendly, catering to both beginners and experts in data analysis.

## Usage

To use this pipeline, follow these steps:

1. Clone or download this repository to your local machine.
2. Place the JSON files you want to process in the same directory as the scripts.
3. Open the `main.py` script and replace the placeholder list of JSON files (`json_files`) with the list of your actual JSON files.
4. Run the `main.py` script. The script will process the JSON files and create a dictionary of DataFrames, which are then ready for analysis or can be saved in your desired format (CSV, Excel, SQL database, etc.)

## Target Audience

This pipeline is a valuable resource for:

- **Data Scientists and Analysts:** With preprocessed and structured data, data scientists and analysts can focus on generating insights rather than on cleaning and formatting data.
- **Real Estate Enthusiasts:** This project provides valuable data on real estate projects, which can be used for trend analysis, market research, and investment decisions.
- **Government and Corporates:** The data extracted can be used for policy-making, strategic planning, competition analysis, and other corporate decisions.
- **Students:** This project can serve as a practical case study for students learning data science, data analysis, or real estate management.

Join us in this exciting journey of transforming raw data into meaningful insights! Explore the [GujRera website](https://gujrera.gujarat.gov.in/), view the project on [this link](http://3.111.75.239/#/), and access the registration portal [here](https://gujrerar1.gujarat.gov.in/).
