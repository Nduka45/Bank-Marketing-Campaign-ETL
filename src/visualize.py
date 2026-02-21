# src/visualize.py
import os
import logging
import matplotlib.pyplot as plt

REPORT_PATH = "reports"

def plot_subscription_rate(df):
    logging.info("Generating subscription rate plot...")
    os.makedirs(REPORT_PATH, exist_ok=True)

    if "campaign_outcome" not in df.columns:
        raise ValueError("No subscription column found ('campaign_outcome')")

    df = df.rename(columns={"campaign_outcome": "subscribed"})
    counts = df["subscribed"].value_counts()

    plt.figure()
    plt.bar(counts.index.astype(str), counts.values, color="orange")
    plt.title("Subscription Rate")
    plt.xlabel("Subscribed")
    plt.ylabel("Count")
    plt.savefig(os.path.join(REPORT_PATH, "subscription_rate.png"))
    plt.close()

    logging.info("Plot saved at %s", os.path.join(REPORT_PATH, "subscription_rate.png"))
