import pandas as pd

def clean_results(results: list[dict]) -> pd.DataFrame:
    """Take raw results list, build a DataFrame, and apply all cleaning rules."""
    df = pd.DataFrame(results)

    # Remove duplicate domains keeping the highest score
    df = df.sort_values("score", ascending=False)
    df = df.drop_duplicates(subset="site", keep="first")

    # Cap skill mention total at 20 to prevent noisy sites skewing analysis
    df["score"] = df["score"].clip(upper=20)

    # Ensure no negative scores
    df["score"] = df["score"].clip(lower=0)

    # Replace empty strings with None for clarity
    df["skills"] = df["skills"].replace("", None)
    df["skill_detail"] = df["skill_detail"].replace("", None)
    df["url"] = df["url"].replace("", None)

    # Reset index cleanly
    df = df.reset_index(drop=True)

    return df