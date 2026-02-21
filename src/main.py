import os
from pathlib import Path

# Relative imports because src is a package
from .visualize import plot_age_distribution, plot_subscription_rate
from .transform import (
    load_csv,
    clean_columns,
    clean_bank_data,
    clean_campaign_data,
    clean_economics_data
)

# Get project root automatically
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_PATH = BASE_DIR / "data" / "raw"
OUTPUT_PATH = BASE_DIR / "data" / "processed"

def run_pipeline():
    print("Starting ETL pipeline...")

    # Extract
    bank_df = load_csv(RAW_PATH / "bank_marketing.csv")
    campaign_df = load_csv(RAW_PATH / "campaign.csv")
    economics_df = load_csv(RAW_PATH / "economics.csv")

    print("Files loaded.")

    # Standardize columns
    bank_df = clean_columns(bank_df)
    campaign_df = clean_columns(campaign_df)
    economics_df = clean_columns(economics_df)

    # Transform
    bank_df = clean_bank_data(bank_df)
    campaign_df = clean_campaign_data(campaign_df)
    economics_df = clean_economics_data(economics_df)

    print("Data cleaned.")

    # Generate visuals
    plot_age_distribution(bank_df)

    if "y" in bank_df.columns:
        bank_df.rename(columns={"y": "subscribed"}, inplace=True)

    plot_subscription_rate(bank_df)

    # Save outputs
    os.makedirs(OUTPUT_PATH, exist_ok=True)

    bank_df.to_csv(OUTPUT_PATH / "bank_cleaned.csv", index=False)
    campaign_df.to_csv(OUTPUT_PATH / "campaign_cleaned.csv", index=False)
    economics_df.to_csv(OUTPUT_PATH / "economics_cleaned.csv", index=False)

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    run_pipeline()
