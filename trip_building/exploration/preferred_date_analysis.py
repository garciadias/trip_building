# %%
from trip_building.exploration.create_date_analysis import plot_requests_by_count
from trip_building.load_data import load_raw_data

# %%

if __name__ == "__main__":
    print("🚀 Running scrip to plot the number of trips by preferred date per day of the week. 📈 ")
    # Set the output path
    output_dir = "report/figures/"
    # Load the data
    print("\t🗃 Loading the data...")
    data_path = "data/raw/reporting-trip-request-extract.csv"
    types_json_path = "trip_building/reporting_trip_request_extract_types.json"
    df = load_raw_data(data_path, types_json_path)
    # Print date range on the format: [day of the week] %YYYY-dd-mm hh:min:ss
    print("\t📅 Preferred data range:")
    print(f"\t\tStart date: {df['createtripformsubmission_preferreddate'].min().strftime('%A %Y-%m-%d %H:%M:%S')}")
    print(f"\t\tEnd date: {df['createtripformsubmission_preferreddate'].max().strftime('%A %Y-%m-%d %H:%M:%S')}")
    print("\t✅ Data loaded successfully.")
    # Calculate the number of trips by preferred day of the week and the percentage of the total requests
    print(
        "\t📊 Calculating the number of trips by preferred day of the week and the percentage of the total requests..."
    )
    request_by_day_of_week = df["createtripformsubmission_preferreddate"].dt.day_name().value_counts()
    request_by_day_of_week_percent = request_by_day_of_week / request_by_day_of_week.sum()
    # Calculate the number of trips by preferred Month of the Year and the percentage of the total requests
    request_by_moth_of_year = df["createtripformsubmission_preferreddate"].dt.month_name().value_counts()
    request_by_moth_of_year_percent = request_by_moth_of_year / request_by_moth_of_year.sum()
    print("\t✅ Calculations completed successfully.")
    # Plot the number of trips by preferred day of the week and the percentage of the total requests
    print("\t📈 Plotting the number of trips by preferred day of the week and the percentage of the total requests...")
    plot_requests_by_count(
        request_by_day_of_week,
        request_by_day_of_week_percent,
        output_path=f"{output_dir}/preferred_date_by_day_of_week.png",
        plot_title="Number of trips by preferred day of the week",
        x_title="Day of the week",
    )
    # Plot the number of trips by preferred Month of the year and the percentage of the total requests
    plot_requests_by_count(
        request_by_moth_of_year,
        request_by_moth_of_year_percent,
        output_path=f"{output_dir}/preferred_date_by_moth_of_year.png",
        plot_title="Number of trips by preferred month of the year",
        x_title="Month of the year",
    )
    print("\t✅ Plot generated successfully.")
    print("\t📌 Plot saved at {output_path}.")
