# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 13:06:59 2024

@author: falih
"""
# import json for processing json files

import json

import pandas as pd

# method #1 to read json files
# open the json file
json_file = open('loan_data_json.json')

# loading the json file

data = json.load('json_file')
