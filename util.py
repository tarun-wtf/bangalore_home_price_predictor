import pickle
import json
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

# Get the absolute path of the current file (util.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    columns_path = os.path.join(ARTIFACTS_DIR, "columns.json")
    model_path = os.path.join(ARTIFACTS_DIR, "banglore_home_prices_model.pickle")

    # Load columns.json
    with open(columns_path, "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    # Load model only once
    if __model is None:
        with open(model_path, "rb") as f:
            __model = pickle.load(f)

    print("loading saved artifacts...done")


def get_location_names():
    return __locations


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
