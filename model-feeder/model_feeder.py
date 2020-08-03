"""
    ModelFeeder Todo List
     1. Read the JSON data 
     2. Load events into window
     3. Convert events using the category_encoders lib
     4. Write window to json?
"""

import json
import numpy as np
from pprint import pprint
from pathlib import Path
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from operator import attrgetter
from sklearn.datasets import load_boston

I = 1
PATH_TO_MOCK_DATA = "mock-dataset/mock_data.json"
WINDOW_SIZE = 30 * I

def sort_events(data):
    data.sort(key=lambda e: e['timestamp'])
    pass

def convert_list_of_dicts(lod, keylist):
    return [[row[key] for key in keylist] for row in lod]

def encode(data):
    # Add a variable that indicates time difference from previous data point?
    # Change timestamp variable
    X = np.stack(data) # Convert to numpy array
    Y = np.delete(X, 3, axis=1)
    enc = OneHotEncoder()
    transformed_data = enc.fit_transform(Y).toarray() # Results in 333 "input nodes", without timestamp, 58 "input nodes"
    inversed_data = enc.inverse_transform(transformed_data)
    pprint(transformed_data)
    pprint(inversed_data)
    pass

def read_into_window(data, index):
    pass    

def read_JSON_file(path):
    pass

with open(Path(PATH_TO_MOCK_DATA)) as json_file:
    data = json.load(json_file)
    sort_events(data)
    events = convert_list_of_dicts(data, ['event', 'sensor', 'sensor_group', 'timestamp'])
    encode(events)
