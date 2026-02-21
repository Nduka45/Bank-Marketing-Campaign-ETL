# src/visualize.py
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Folder to save plots
REPORT_PATH = "reports"
os.makedirs(REPORT_PATH, exist_ok=True)

def _show_and_save(fig, filename):
    """Helper: show plot interactively then save it."""
    plt.show()  # Display the plot
    fig.savefig(os.path.join(REPORT_PATH, filename))
    plt.close(fig)

def plot_subscription_rate(df):
    fig, ax = plt.subplots()
    counts = df['campaign_outcome'].value_counts()
    ax.bar(counts.index, counts.values, color='orange')
    ax.set_title("Overall Subscription Rate")
    ax.set_xlabel("Subscribed")
    ax.set_ylabel("Count")
    _show_and_save(fig, "subscription_rate.png")

def plot_subscription_by_age(df):
    fig, ax = plt.subplots()
    sns.histplot(data=df, x='age', hue='campaign_outcome', multiple='stack', palette=['red','green'], ax=ax)
    ax.set_title("Subscription by Age")
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")
    _show_and_save(fig, "subscription_by_age.png")

def plot_subscription_by_job(df):
    job_counts = df.groupby(['job','campaign_outcome']).size().unstack(fill_value=0)
    job_counts['total'] = job_counts.sum(axis=1)
    job_counts = job_counts.sort_values('total', ascending=False)
    fig, ax = plt.subplots()
    job_counts[['yes','no']].plot(kind='barh', stacked=True, color=['green','red'], legend=True, ax=ax)
    ax.set_title("Subscription by Job")
    ax.set_xlabel("Number of Customers")
    ax.set_ylabel("Job")
    _show_and_save(fig, "subscription_by_job.png")

def plot_contact_duration_vs_subscription(df):
    fig, ax = plt.subplots()
    sns.boxplot(data=df, x='campaign_outcome', y='contact_duration', palette=['red','green'], ax=ax)
    ax.set_title("Contact Duration vs Subscription")
    ax.set_xlabel("Subscribed")
    ax.set_ylabel("Call Duration (seconds)")
    _show_and_save(fig, "contact_duration_vs_subscription.png")

def plot_previous_contacts_vs_subscription(df):
    previous_counts = df.groupby(['previous_campaign_contacts','campaign_outcome']).size().unstack(fill_value=0)
    fig, ax = plt.subplots()
    previous_counts[['yes','no']].plot(kind='bar', stacked=True, color=['green','red'], legend=True, ax=ax)
    ax.set_title("Subscription by Previous Campaign Contacts")
    ax.set_xlabel("Number of Previous Contacts")
    ax.set_ylabel("Number of Customers")
    _show_and_save(fig, "subscription_by_previous_contacts.png")

def plot_subscription_by_month(df):
    month_counts = df.groupby(['month','campaign_outcome']).size().unstack(fill_value=0)
    fig, ax = plt.subplots()
    month_counts[['yes','no']].plot(kind='bar', stacked=True, color=['green','red'], legend=True, ax=ax)
    ax.set_title("Subscription by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Customers")
    _show_and_save(fig, "subscription_by_month.png")

def generate_all_plots(df):
    plot_subscription_rate(df)
    plot_subscription_by_age(df)
    plot_subscription_by_job(df)
    plot_contact_duration_vs_subscription(df)
    plot_previous_contacts_vs_subscription(df)
    plot_subscription_by_month(df)
