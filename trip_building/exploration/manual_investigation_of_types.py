"""Manually inspect the types of the columns in the reporting_trip_request_extract.csv file"""

# %%
import json
from pathlib import Path

import pandas as pd
from IPython.display import display

# %%

# Load the data
data_path = Path("data/raw/reporting-trip-request-extract.csv")
df = pd.read_csv(data_path)
df.select_dtypes(include="object").head()

# Inspect the types of the object columns on the dataframe
# %%
reporting_trip_request_extract_types = {}
for col, dtype in df.select_dtypes(include="object").dtypes.items():
    print(f"================= Column: {col} ================")
    display(df[col].describe())
    print("\n")
    display(df[col].sample(5))
    var_type = input(f"Enter the type for {col}: ")
    reporting_trip_request_extract_types[col] = var_type
# Accept the types presented by pandas
# %%
reporting_trip_request_extract_types.update(
    {col: str(var_type) for col, var_type in df.select_dtypes(exclude="object").dtypes.items()}
)
# Save the types in a json file
# %%
json.dump(
    reporting_trip_request_extract_types,
    sort_keys=True,
    indent=4,
    separators=(",", ": "),
    fp=open("trip_building/reporting_trip_request_extract_types.json", "w"),
)
