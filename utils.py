# Create full dataset

# Imports
import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv
from cassandra.cluster import Cluster

def collect_data_filepaths(sub_directory):
    """
    Searches a given sub-directory of the current working directory, collecting filepaths
    and returning in a list.
    
    Arguments:
    sub_directory -- subdirectory where data files are contained, prefixed with forward slash
    
    Returns:
    file_paths -- list of file paths from given sub-directory.
    """
    filepath = os.getcwd() + sub_directory
    for root, dirs, files in os.walk(filepath):
        file_paths = glob.glob(os.path.join(root,'*'))
    return file_paths



def create_combined_dataset(file_path_list):
    """
    Takes a file path, reads all csv files in the path, and appends the contents
    to an empty list which is returned.
    
    Arguments:
    file_path_list -- file path to iterate through for csv files
    
    Returns:
    full_data_rows_list -- list containing rows of data from csv files in given filepath
    """
    full_data_rows_list = []
    for f in file_path_list: 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)
        for line in csvreader:
            full_data_rows_list.append(line)
    return full_data_rows_list


def get_data():
    """
    Implements functions to collect filepaths from given sub-directory, and
    concatenates this into a list of data, returned.
    
    Returns:
    data -- list of all combined data from given filepaths
    """
    files = collect_data_filepaths(sub_directory = '/event_data')
    data = create_combined_dataset(files)
    return data


            

