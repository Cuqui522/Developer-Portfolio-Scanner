import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

def generate_charts(df: pd.DataFrame, output_dir: str) -> None:
    """Generate and save skill frequency and availability charts from results DataFrame."""
    os.makedirs(output_dir, exist_ok=True)
    _plot_top_skills(df, output_dir)
    _plot_availability(df, output_dir)
    print(f"📊 Charts saved to {output_dir}")


def _plot_top_skills(df: pd.DataFrame, output_dir: str) -> None:
    """Generate a bar chart of the most common skills across all scanned sites."""
    # Count how many sites mention each skill
    skill_counts = Counter()
    for skills in df["skills"].dropna():
        for skill in skills.split(", "):
            skill = skill.strip()
            if skill:
                skill_counts[skill] += 1

    if not skill_counts:
        print("⚠️  No skill data to chart.")
        return

    # Take top 10 skills
    top_skills = dict(skill_counts.most_common(10))

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(list(top_skills.keys()), list(top_skills.values()), color="steelblue")
    ax.set_xlabel("Number of Sites")
    ax.set_title("Top Skills Across Scanned Developer Portfolios")
    ax.invert_yaxis()  # Most common skill at the top
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "skills_chart.png"))
    plt.close()


def _plot_availability(df: pd.DataFrame, output_dir: str) -> None:
    """Generate a pie chart showing the ratio of available vs unavailable developers."""
    available = df["available"].sum()
    unavailable = len(df) - available

    if available == 0 and unavailable == 0:
        print("⚠️  No availability data to chart.")
        return

    labels = ["Open to Work", "Not Available"]
    sizes = [available, unavailable]
    colors = ["#2ecc71", "#e74c3c"]

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    ax.set_title("Developer Availability")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "availability_chart.png"))
    plt.close()