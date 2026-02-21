# src/visualize.py
import os
import matplotlib.pyplot as plt

REPORT_PATH = "reports"

def plot_subscription_rate(df):
    os.makedirs(REPORT_PATH, exist_ok=True)
    if "campaign_outcome" in df.columns:
        df = df.rename(columns={"campaign_outcome": "subscribed"})
    counts = df["subscribed"].value_counts()
    plt.figure()
    plt.bar(counts.index.astype(str), counts.values, color="orange")
    plt.title("Subscription Rate")
    plt.xlabel("Subscribed")
    plt.ylabel("Count")
    plt.savefig(os.path.join(REPORT_PATH, "subscription_rate.png"))
    plt.close()

def plot_age_distribution(df):
    os.makedirs(REPORT_PATH, exist_ok=True)
    counts = df["age"].value_counts().sort_index()
    plt.figure()
    plt.bar(counts.index, counts.values, color="blue")
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.savefig(os.path.join(REPORT_PATH, "age_distribution.png"))
    plt.close()
