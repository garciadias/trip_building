import json
from pathlib import Path
from typing import Union

import pandas as pd


def load_raw_data(data_path: Union[str, Path], types_json_path: Union[str, Path]) -> pd.DataFrame:
    """Load the raw data from the path.

    Parameters
    ----------
    data_path : Path
        The path to the raw data.

    types_json_path : Path
        The path to the json file containing the types of the columns in the raw data.

    Returns
    -------
    pd.DataFrame
        The data.
    """
    # Load the data
    data_path = Path(data_path)
    with open(types_json_path) as json_file:
        pre_inspection_types = json.load(json_file)
    date_cols = [col for col, var_type in pre_inspection_types.items() if "date" in var_type.lower()]
    # remove date_cols from pre_inspection_types
    for col in date_cols:
        pre_inspection_types.pop(col)
    df = pd.read_csv(data_path, parse_dates=date_cols)
    df = df.astype(pre_inspection_types)
    return df
