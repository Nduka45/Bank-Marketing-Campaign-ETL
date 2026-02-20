#import os and define the function for data transformation

import os
from transform import (
    load_csv,
    clean_columns,
    clean_bank_data,
    clean_campaign_data,
    clean_economics_data
)

# define the path to store the data after processing: ouput path
RAW_PATH = "data/raw/"
OUTPUT_PATH = "data/processed/"


def run_pipeline():
    print("Starting ETL pipeline...")

    # Extract
    bank_df = load_csv(os.path.join(RAW_PATH, "bank_marketing.csv"))
    campaign_df = load_csv(os.path.join(RAW_PATH, "campaign.csv"))
    economics_df = load_csv(os.path.join(RAW_PATH, "economics.csv"))

    print("Files loaded.")

    # Standardize columns
    bank_df = clean_columns(bank_df)
    campaign_df = clean_columns(campaign_df)
    economics_df = clean_columns(economics_df)

    # Transform per dataset
    bank_df = clean_bank_data(bank_df)
    campaign_df = clean_campaign_data(campaign_df)
    economics_df = clean_economics_data(economics_df)

    print("Data cleaned.")

    # Load (Save cleaned files)
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    bank_df.to_csv(os.path.join(OUTPUT_PATH, "bank_cleaned.csv"), index=False)
    campaign_df.to_csv(os.path.join(OUTPUT_PATH, "campaign_cleaned.csv"), index=False)
    economics_df.to_csv(os.path.join(OUTPUT_PATH, "economics_cleaned.csv"), index=False)

    print("ETL pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()
