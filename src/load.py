import logging
from config import PROCESSED_PATH

def load_data(client_df, campaign_df, outcome_df):
    logging.info("Loading data to CSV...")

    client_df.to_csv(f"{PROCESSED_PATH}client_data.csv", index=False)
    campaign_df.to_csv(f"{PROCESSED_PATH}campaign_data.csv", index=False)
    outcome_df.to_csv(f"{PROCESSED_PATH}loan_outcomes.csv", index=False)

    logging.info("Files saved successfully.")
