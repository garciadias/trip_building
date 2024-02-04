"""Uses ydata_profiling to generate a report on the data."""

# %%
import webbrowser

from ydata_profiling import ProfileReport

from trip_building.load_data import load_raw_data

if __name__ == "__main__":
    print("🚀 Creating ydata-Profiling Reports")
    # Set the output path
    print("\t🗃 Loading the data...")
    data_path = "data/raw/reporting-trip-request-extract.csv"
    types_json_path = "trip_building/reporting_trip_request_extract_types.json"
    output_report_path = "report/pandas-profiling/reporting_trip_request_extract_report.html"
    output_failed_report_path = "report/pandas-profiling/reporting_trip_request_extract_failed_report.html"
    # Load the data
    df = load_raw_data(data_path, types_json_path)
    print("\t✅ Data loaded successfully.")
    # Generate the report
    print("\t📊 Generating the report...")
    profile = ProfileReport(df, title="Byway Trip Building", explorative=True)
    # Export the report as an html file
    profile.to_file(output_report_path)
    print("\t✅ Report generated successfully.")
    # Profile failed trips
    print("\t📊 Generating the failed report...")
    df_failed = df[~df["success"]]
    profile_failed = ProfileReport(df_failed, title="Byway Trip Building Failed Trips")
    profile_failed.to_file(output_failed_report_path)
    print("\t✅ Failed report generated successfully.")
    # Open the reports
    print("\t📌 Reports saved at\t\t\n{output_report_path}\t\t\n{output_failed_report_path}.")
    print("\t📌 Reports opened in your default web browser.")
    webbrowser.open(output_failed_report_path)
    webbrowser.open(output_report_path)
