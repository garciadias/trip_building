# %%

import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display

from trip_building.load_data import load_raw_data

# %%
# Load the raw data
data_path = "data/raw/reporting-trip-request-extract.csv"
types_json_path = "trip_building/reporting_trip_request_extract_types.json"
df = load_raw_data(data_path, types_json_path)
# %%
top_cities = df["createtripformsubmission_closestcity"].value_counts().head(5)

# %%
for i, city in enumerate(top_cities.index):
    print(city)
    cols = ["createtripformsubmission_closestcity", "region", "requestdate"]
    filter_city = df["createtripformsubmission_closestcity"] == city
    count_per_city = (
        df[filter_city][cols]
        .groupby(["createtripformsubmission_closestcity", "region"])
        .count()
        .sort_values(by="requestdate", ascending=False)
    )
    display(count_per_city.head(5))
    if i > 5:
        break
# %%
# get all for Paris

# %%
df["createtripid_region"].value_counts().sort_values(ascending=False).head(5)
# %%

error_cols = [col for col in df.columns if "error" in col.lower() or "fail" in col.lower()]
error_cols.remove("failtimeseconds")
# %%
for col in error_cols:
    print(col)
    counts = df[~df["success"]][col].value_counts()
    percent = counts / counts.sum()
    print(counts)
    plt.bar(counts.index, counts)
    for i, value in enumerate(percent):
        plt.text(
            i,
            counts.iloc[i] * 1.03,
            f"{value:.2%}",
            ha="center",
            va="bottom",
            rotation=90,
            fontsize=12,
        )
    plt.title(col)
    plt.show()
# %%
# count values equal zero or false and aggregate other values in a single category
error_counts = {}
for col in error_cols:
    error_counts[col] = df[~df["success"]][col].apply(lambda x: 1 if x else 0).value_counts()
ALL_ERRORS = pd.DataFrame(error_counts).T
ALL_ERRORS = ALL_ERRORS.fillna(0).sort_values(by=1, ascending=False)
ALL_ERRORS = ALL_ERRORS.rename(columns={0: "zero", 1: "non_zero"})

# %%
ALL_ERRORS["non_zero_percent"] = 100 * (ALL_ERRORS["non_zero"] / 130)
ALL_ERRORS["non_zero_percent"] = ALL_ERRORS["non_zero_percent"].round(2)
ALL_ERRORS["non_zero_percent"] = ALL_ERRORS["non_zero_percent"].astype(str) + "%"
# %%
display(ALL_ERRORS[["non_zero", "non_zero_percent"]])
# %%
df[~df["success"] & df["region"].eq("Highlands & Islands")][error_cols]
# %%
for error in error_cols:
    display(df[~df["success"] & df[error]].groupby("region").size())
# %%
100 * (31 / 5000)
# %%
interests = (
    df["array_to_string"]
    .str.split(pat=",", expand=True)
    .apply(lambda x: x.value_counts(), axis=1)
    .fillna(0)
    .astype(int)
)

# %%
