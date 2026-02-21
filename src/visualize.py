# src/visualize.py
#import matplotlib, loggings and os for visualization

import matplotlib.pyplot as plt
import logging
import os

REPORT_PATH = "reports/figures/"

def plot_subscription_rate(outcome_df):
    logging.info("Generating subscription rate plot...")

    os.makedirs(REPORT_PATH, exist_ok=True)

    if "subscribed" in outcome_df.columns:
        counts = outcome_df["subscribed"].value_counts()
    elif "y" in outcome_df.columns:
        counts = outcome_df["y"].value_counts()
    else:
        raise ValueError("No subscription column found ('subscribed' or 'y')")

    plt.figure()
    plt.bar(counts.index.astype(str), counts.values)
    plt.title("Loan Subscription Outcome")
    plt.xlabel("Subscribed")
    plt.ylabel("Count")
    plt.savefig(f"{REPORT_PATH}subscription_rate.png")
    plt.close()
