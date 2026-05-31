"""
Data Analyst Salary Analysis
=============================
Exploratory Data Analysis (EDA) of global Data Analyst / Data Science salaries.

This script loads the dataset, cleans it, derives key insights, and produces
visualizations that answer common questions for aspiring data analysts:
  - How does salary scale with experience level?
  - Which job titles and countries pay the most?
  - Does remote work correlate with higher pay?

Author: Sangam Krishna (@SnakeEye-sudo)
License: MIT
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = os.path.join("data", "data_analyst_salaries.csv")
OUTPUT_DIR = "reports"

EXPERIENCE_LABELS = {
    "EN": "Entry",
    "MI": "Mid",
    "SE": "Senior",
    "EX": "Executive",
}


def load_data(path=DATA_PATH):
    """Load the salary dataset into a pandas DataFrame."""
    df = pd.read_csv(path)
    return df


def clean_data(df):
    """Clean and enrich the raw dataset."""
    df = df.drop_duplicates()
    df = df.dropna(subset=["salary_usd"])
    df["experience"] = df["experience_level"].map(EXPERIENCE_LABELS)
    df["is_remote"] = df["remote_ratio"] == 100
    return df


def summary_statistics(df):
    """Print high-level summary statistics."""
    print("Total records:", len(df))
    print("Average salary (USD): {:,.0f}".format(df["salary_usd"].mean()))
    print("Median salary (USD): {:,.0f}".format(df["salary_usd"].median()))
    print("\nSalary by experience level:")
    print(df.groupby("experience")["salary_usd"].mean().round(0))


def salary_by_experience(df):
    """Return average salary grouped by experience level."""
    order = ["Entry", "Mid", "Senior", "Executive"]
    grouped = df.groupby("experience")["salary_usd"].mean()
    grouped = grouped.reindex([x for x in order if x in grouped.index])
    return grouped


def top_paying_titles(df, n=5):
    """Return the top n highest paying job titles by average salary."""
    return df.groupby("job_title")["salary_usd"].mean().sort_values(ascending=False).head(n)


def salary_by_country(df, n=8):
    """Return average salary by company location."""
    return df.groupby("company_location")["salary_usd"].mean().sort_values(ascending=False).head(n)


def remote_vs_onsite(df):
    """Compare average salary for remote vs non-remote roles."""
    return df.groupby("is_remote")["salary_usd"].mean()


def plot_salary_by_experience(df, output_dir=OUTPUT_DIR):
    """Create and save a bar chart of average salary by experience."""
    os.makedirs(output_dir, exist_ok=True)
    grouped = salary_by_experience(df)
    plt.figure(figsize=(8, 5))
    grouped.plot(kind="bar", color="#2b8a3e")
    plt.title("Average Data Analyst Salary by Experience Level")
    plt.xlabel("Experience Level")
    plt.ylabel("Average Salary (USD)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    out_path = os.path.join(output_dir, "salary_by_experience.png")
    plt.savefig(out_path, dpi=120)
    plt.close()
    print("Saved chart:", out_path)


def main():
    df = load_data()
    df = clean_data(df)

    summary_statistics(df)

    print("\nTop paying job titles:")
    print(top_paying_titles(df).round(0))

    print("\nTop paying countries:")
    print(salary_by_country(df).round(0))

    print("\nRemote vs on-site average salary:")
    print(remote_vs_onsite(df).round(0))

    plot_salary_by_experience(df)


if __name__ == "__main__":
    main()
