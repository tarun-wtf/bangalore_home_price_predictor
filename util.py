import pickle
import json
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

# Get absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTIFACTS_DIR = os.path.join(BASE_DIR, "artifacts")

def get_estimated_price(location, sqft, bhk, bath):
    # Normalize location
    location = location.strip().lower()

    # Create lowercase version of columns for matching
    data_cols_lower = [col.lower() for col in __data_columns]

    # Find index safely
    try:
        loc_index = data_cols_lower.index(location)
    except ValueError:
        loc_index = -1

    # Create input vector
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1

    # Prediction
    return round(__mod
