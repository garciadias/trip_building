# %%
import matplotlib.pyplot as plt
import pandas as pd

from trip_building.constants import BYWAY_COLORS
from trip_building.load_data import load_raw_data


def plot_requests_by_count(
    request_by_day_of_week: pd.Series,
    request_by_day_of_week_percent: pd.Series,
    output_path: str,
    plot_title: str = "Number of requests by day of the week",
    x_title: str = "Day of the week",
) -> None:
    """Plot the number of requests by day of the week and the percentage of the total requests.

    Parameters
    ----------
    request_by_day_of_week : pd.Series
        The number of requests by day of the week.

    request_by_day_of_week_percent : pd.Series
        The percentage of the total requests by day of the week.

    output_path : str, optional
        The path to save the plot.

    Returns
    -------
    None
    """
    _, ax = plt.subplots()
    ax.bar(
        request_by_day_of_week.index,
        request_by_day_of_week,
        color=BYWAY_COLORS["orange"],
    )
    ax.set_title(plot_title.title())
    ax.set_ylabel("Number of requests".title())
    ax.set_xlabel(x_title.title())
    # add percentage labels to the top of the bars
    rotation = 90 if len(request_by_day_of_week) > 10 else 0
    position_factor = 1.03 if len(request_by_day_of_week) > 10 else 1.0
    for i, value in enumerate(request_by_day_of_week_percent):
        ax.text(
            i,
            request_by_day_of_week.iloc[i] * position_factor,
            f"{value:.2%}",
            ha="center",
            va="bottom",
            rotation=rotation,
            fontsize=12,
        )  # Add the percentage of the total requests
    if len(request_by_day_of_week) > 10:
        plt.ylim(0, request_by_day_of_week.max() * 1.3)
        plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()


# %%

if __name__ == "__main__":
    print("🚀 Running scrip to plot the number of requests per day of the week. 📈 ")
    # Set the output path
    output_dir = "report/figures/"
    # Load the data
    print("\t🗃 Loading the data...")
    data_path = "data/raw/reporting-trip-request-extract.csv"
    types_json_path = "trip_building/reporting_trip_request_extract_types.json"
    df = load_raw_data(data_path, types_json_path)
    # Print date range on the format: [day of the week] %YYYY-dd-mm hh:min:ss
    print("\t📅 Date range of the data:")
    print(f"\t\tStart date: {df['requestdate'].min().strftime('%A %Y-%m-%d %H:%M:%S')}")
    print(f"\t\tEnd date: {df['requestdate'].max().strftime('%A %Y-%m-%d %H:%M:%S')}")
    print("\t✅ Data loaded successfully.")
    # Calculate the number of requests by day of the week and the percentage of the total requests
    print("\t📊 Calculating the number of requests by day of the week and the percentage of the total requests...")
    request_by_day_of_week = df["requestdate"].dt.day_name().value_counts()
    request_by_day_of_week_percent = request_by_day_of_week / request_by_day_of_week.sum()
    # Calculate the number of requests by hour of the day and the percentage of the total requests
    request_by_hour_of_day = df["requestdate"].dt.hour.value_counts().sort_index()
    request_by_hour_of_day_percent = request_by_hour_of_day / request_by_hour_of_day.sum()
    print("\t✅ Calculations completed successfully.")
    # Plot the number of requests by day of the week and the percentage of the total requests
    print("\t📈 Plotting the number of requests by day of the week and the percentage of the total requests...")
    plot_requests_by_count(
        request_by_day_of_week,
        request_by_day_of_week_percent,
        output_path=f"{output_dir}/requests_by_day_of_week.png",
    )
    # Plot the number of requests by Month of the year and the percentage of the total requests
    plot_requests_by_count(
        request_by_hour_of_day,
        request_by_hour_of_day_percent,
        output_path=f"{output_dir}/requests_by_hour_of_day.png",
        plot_title="Number of requests by hour of the day",
        x_title="Hour of the day",
    )
    print("\t✅ Plot generated successfully.")
    print("\t📌 Plot saved at {output_path}.")
