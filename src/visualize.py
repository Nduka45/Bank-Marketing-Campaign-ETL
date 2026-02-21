# src/visualize.py
import matplotlib.pyplot as plt
import logging
import os

# Ensure logging shows info messages
logging.basicConfig(level=logging.INFO)

REPORT_PATH = "reports/figures/"

def plot_age_distribution(df):
    logging.info("Generating age distribution plot...")

    os.makedirs(REPORT_PATH, exist_ok=True)

    if "age" not in df.columns:
        raise ValueError("No 'age' column found in dataframe")

    plt.figure()
    plt.hist(df["age"], bins=20, color="skyblue", edgecolor="black")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.savefig(os.path.join(REPORT_PATH, "age_distribution.png"))
    plt.close()

def plot_subscription_rate(df):
    logging.info("Generating subscription rate plot...")

    os.makedirs(REPORT_PATH, exist_ok=True)

    # Rename 'y' to 'subscribed' if present
    if "subscribed" not in df.columns and "y" in df.columns:
        df = df.rename(columns={"y": "subscribed"})

    if "subscribed" not in df.columns:
        raise ValueError("No subscription column found ('subscribed' or 'y')")

    counts = df["subscribed"].value_counts()

    plt.figure()
    plt.bar(counts.index.astype(str), counts.values, color="orange")
    plt.title("Subscription Rate")
    plt.xlabel("Subscribed")
    plt.ylabel("Count")
    plt.savefig(os.path.join(REPORT_PATH, "subscription_rate.png"))
    plt.close()
