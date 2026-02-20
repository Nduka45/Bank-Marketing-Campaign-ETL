import matplotlib.pyplot as plt
import logging
import os

REPORT_PATH = "reports/figures/"

def plot_age_distribution(client_df):
    logging.info("Generating age distribution plot...")

    os.makedirs(REPORT_PATH, exist_ok=True)

    plt.figure()
    plt.hist(client_df['age'], bins=20)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.savefig(f"{REPORT_PATH}age_distribution.png")
    plt.close()

def plot_subscription_rate(outcome_df):
    logging.info("Generating subscription rate plot...")

    os.makedirs(REPORT_PATH, exist_ok=True)

    counts = outcome_df['subscribed'].value_counts()

    plt.figure()
    plt.bar(counts.index.astype(str), counts.values)
    plt.title("Loan Subscription Outcome")
    plt.xlabel("Subscribed")
    plt.ylabel("Count")
    plt.savefig(f"{REPORT_PATH}subscription_rate.png")
    plt.close()
