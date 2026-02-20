import pandas as pd
import logging
from config import RAW_DATA_PATH

def extract_data():
    logging.info("Extracting data...")
    df = pd.read_csv(RAW_DATA_PATH)
    logging.info(f"Extracted {len(df)} rows.")
    return df
