import os
import numpy as np 
import pandas as pd
import pickle
import logging
from sklearn.ensemble import RandomForestClassifier

# ensure the "logs" directory exists
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)

# logging configuration
logger = logging.getLogger('model_training')
logger.setLevel('DEBUG')

# console_handler
console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

# file_handler
log_file_path = os.path.join(log_dir, 'model_training.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

# use of formatter for the log details format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)


# data loading
def load_data(file_path:str) -> pd.DataFrame:
    """
    Load data from a CSV file.
    
    :param file_path: path to the csv file
    :return: Loaded DataFrame
    """
    try:
        pass
    except pd.errors.ParserError as e:
        pass
    except FileNotFoundError as e:
        pass
    except Exception as e:
        pass