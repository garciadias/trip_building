"""Analyse the preferences of the users regarding the experiences they want to have during their trip."""

# %%
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from trip_building.constants import BYWAY_COLORS
from trip_building.load_data import load_raw_data


def unfold_array_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """Unfold a column containing arrays into a dataframe with one column per array element.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe containing the column to unfold.

    column : str
        The name of the column to unfold.

    Returns
    -------
    pd.DataFrame
        The dataframe of the unfolded columns.
    """
    unfolded = (
        df[column]
        .dropna()
        .str.split(pat=",", expand=True)
        .apply(lambda x: x.value_counts(), axis=1)
        .fillna(0)
        .astype(int)
    )
    return unfolded


def plot_top_experiences_per_col_value(
    df: pd.DataFrame,
    experiences_columns: list,
    col: str,
    col_alias: str,
    top_n: int = 5,
) -> plt.Figure:
    """Plot the top experiences for each value of a column.

    Parameters
    ----------
    df : pd.DataFrame
        The dataframe containing the data to plot.

    col : str
        The name of the column to use to group the data.

    top_n : int, default=5
        The number of top experiences to plot.

    Returns
    -------
    plt.Figure
        The figure containing the plot.
    """
    top_values = df[col].value_counts().head(top_n).index
    experiences_percents = {}
    for label in top_values:
        filter_label = df[col].eq(label)
        experiences = df[filter_label][experiences_columns].sum().sort_values(ascending=False)
        experiences_percent = 100 * (experiences / experiences.sum())
        experiences_percents[label] = experiences_percent
    df_experiences_percents = (
        pd.DataFrame(experiences_percents)
        .stack()
        .reset_index()
        .rename(columns={"level_0": "Experience", "level_1": col_alias, 0: "Percent"})
    )

    fig, ax = plt.subplots(figsize=(16, 9))
    df_experiences_percents["Experience"] = df_experiences_percents["Experience"].str.replace(" ", "\n")
    sns.barplot(
        data=df_experiences_percents,
        palette=list(BYWAY_COLORS.values()),
        hue=col_alias,
        y="Percent",
        x="Experience",
        ax=ax,
    )
    ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0, fontsize=18)
    ax.set_title(f"Preferred experiences by {col_alias}".title(), fontsize=28)
    plt.xticks(rotation=0, ha="center", fontsize=22)
    plt.ylabel("Percent", fontsize=24)
    plt.xlabel("Experience", fontsize=24)
    plt.tight_layout()
    return fig


if __name__ == "__main__":
    print("🏃 Running exploration of the experiences preferences.")
    # Load the raw data
    data_path = "data/raw/reporting-trip-request-extract.csv"
    types_json_path = "trip_building/reporting_trip_request_extract_types.json"
    df = load_raw_data(data_path, types_json_path)
    print("\t✅ Data loaded.")
    # Create different data filters
    print("\t🔍 Analyzing the data.")
    df["region"] = df["region"].str.replace("& ", "\n&")
    df["has_kids"] = (df["createtripformsubmission_childcount"] > 0).map({True: "Kids", False: "No Kids"})
    df["sole_traveler"] = (
        (df["createtripformsubmission_adultcount"] == 1) & (df["createtripformsubmission_childcount"] == 0)
    ).map({True: "Sole traveler", False: "Not sole traveler"})
    df["Single_adult_with_kids"] = (
        (df["createtripformsubmission_adultcount"] == 1) & (df["createtripformsubmission_childcount"] > 0)
    ).map({True: "Single adult with kids", False: "Others"})
    # Unfold the experiences column
    print("\t📊 Unfolding the experiences column.")
    unfolded_experiences = unfold_array_column(df, "array_to_string")
    df = pd.concat([df, unfolded_experiences], axis=1)
    experiences_columns = list(unfolded_experiences.columns)
    experiences_columns.remove("nan")
    COL_ALIASES = {
        "createtripformsubmission_closestcity": "City of departure",
        "region": "Destiny Region",
        "has_kids": "Has kids",
        "sole_traveler": "Sole traveler",
        "Single_adult_with_kids": "Single adult with kids",
    }
    # %%
    # Plot the top experiences for each value of a column
    print("\t📈 Plotting the top experiences for each value of a column.")
    for col, alias in COL_ALIASES.items():
        print(f"\t\t📊 Plotting the top experiences for {alias}.")
        fig = plot_top_experiences_per_col_value(df, experiences_columns, col, alias)
        plt.savefig(f"report/figures/top_experiences_per_{col}.png")
        plt.close(fig)
    print("✅ Exploration of the experiences preferences done.")
    print("🗃 Figure saved in report/figures.")
