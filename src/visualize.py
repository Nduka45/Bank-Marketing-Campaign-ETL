# src/visualize.py
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Folder to store plots
REPORT_PATH = "reports"
os.makedirs(REPORT_PATH, exist_ok=True)


# Displaying the plots before on GUI and saving it as reports

def _show_and_save(fig, filename):
    """
    Display plot (if GUI available), then save it.
    """
    try:
        plt.show()
    except Exception:
        pass  # In headless mode, just save

    fig.savefig(os.path.join(REPORT_PATH, filename))
    plt.close(fig)


# Overall Subscription against the campaign outcome
def plot_subscription_rate(df):

    if "campaign_outcome" not in df.columns:
        print("Skipping subscription rate plot — column missing.")
        return

    fig, ax = plt.subplots()

    counts = df["campaign_outcome"].value_counts()

    ax.bar(counts.index.astype(str), counts.values, color="orange")
    ax.set_title("Overall Subscription Rate")
    ax.set_xlabel("Subscribed")
    ax.set_ylabel("Count")

    _show_and_save(fig, "subscription_rate.png")


# Subscription by Age
def plot_subscription_by_age(df):

    if "age" not in df.columns or "campaign_outcome" not in df.columns:
        print("Skipping age plot — required columns missing.")
        return

    fig, ax = plt.subplots()

    sns.histplot(
        data=df,
        x="age",
        hue="campaign_outcome",
        multiple="stack",
        palette=["red", "green"],
        ax=ax,
    )

    ax.set_title("Subscription by Age")
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")

    _show_and_save(fig, "subscription_by_age.png")


# The plot of jobs against campaign outcome 
def plot_subscription_by_job(df):

    if "job" not in df.columns or "campaign_outcome" not in df.columns:
        print("Skipping job plot — required columns missing.")
        return

    job_counts = (
        df.groupby(["job", "campaign_outcome"])
        .size()
        .unstack(fill_value=0)
    )

    if "yes" not in job_counts.columns:
        job_counts["yes"] = 0
    if "no" not in job_counts.columns:
        job_counts["no"] = 0

    job_counts["total"] = job_counts.sum(axis=1)
    job_counts = job_counts.sort_values("total", ascending=False)

    fig, ax = plt.subplots()

    job_counts[["yes", "no"]].plot(
        kind="barh",
        stacked=True,
        color=["green", "red"],
        ax=ax,
    )

    ax.set_title("Subscription by Job")
    ax.set_xlabel("Number of Customers")
    ax.set_ylabel("Job")

    _show_and_save(fig, "subscription_by_job.png")


# plotting the duration against campaign outcome
def plot_contact_duration(df):

    if "contact_duration" not in df.columns or "campaign_outcome" not in df.columns:
        print("Skipping duration plot — required columns missing.")
        return

    fig, ax = plt.subplots()

    sns.boxplot(
        data=df,
        x="campaign_outcome",
        y="contact_duration",
        palette=["red", "green"],
        ax=ax,
    )

    ax.set_title("Contact Duration vs Subscription")
    ax.set_xlabel("Subscribed")
    ax.set_ylabel("Call Duration (seconds)")

    _show_and_save(fig, "contact_duration_vs_subscription.png")


# plots for previous contacts
def plot_previous_contacts(df):

    if "previous_campaign_contacts" not in df.columns or "campaign_outcome" not in df.columns:
        print("Skipping previous contacts plot — required columns missing.")
        return

    prev_counts = (
        df.groupby(["previous_campaign_contacts", "campaign_outcome"])
        .size()
        .unstack(fill_value=0)
    )

    if "yes" not in prev_counts.columns:
        prev_counts["yes"] = 0
    if "no" not in prev_counts.columns:
        prev_counts["no"] = 0

    fig, ax = plt.subplots()

    prev_counts[["yes", "no"]].plot(
        kind="bar",
        stacked=True,
        color=["green", "red"],
        ax=ax,
    )

    ax.set_title("Subscription by Previous Campaign Contacts")
    ax.set_xlabel("Previous Contacts")
    ax.set_ylabel("Number of Customers")

    _show_and_save(fig, "subscription_by_previous_contacts.png")


# monthly subscription
def plot_subscription_by_month(df):

    if "month" not in df.columns or "campaign_outcome" not in df.columns:
        print("Skipping month plot — required columns missing.")
        return

    month_counts = (
        df.groupby(["month", "campaign_outcome"])
        .size()
        .unstack(fill_value=0)
    )

    if "yes" not in month_counts.columns:
        month_counts["yes"] = 0
    if "no" not in month_counts.columns:
        month_counts["no"] = 0

    fig, ax = plt.subplots()

    month_counts[["yes", "no"]].plot(
        kind="bar",
        stacked=True,
        color=["green", "red"],
        ax=ax,
    )

    ax.set_title("Subscription by Month")
    ax.set_xlabel("Month")
    ax.set_ylabel("Number of Customers")

    _show_and_save(fig, "subscription_by_month.png")


# generation of all plots
def generate_all_plots(df):
    print("Generating all plots...")

    plot_subscription_rate(df)
    plot_subscription_by_age(df)
    plot_subscription_by_job(df)
    plot_contact_duration(df)
    plot_previous_contacts(df)
    plot_subscription_by_month(df)

    print("All plots generated and saved in 'reports/'")
