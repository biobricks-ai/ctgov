import json
import numpy as np
import os
import pandas as pd
from pathlib import Path
import pyarrow as pa
import pyarrow.parquet as pq

os.makedirs("brick", exist_ok=True)

data_dict = None
pandas_mappings = {
    "string": pd.StringDtype(storage="pyarrow"),
    "integer": 'Int64',
    "boolean": np.bool_,
    "text": pd.StringDtype(storage="pyarrow"),
    "decimal": pd.StringDtype(storage="pyarrow"), # pd.ArrowDtype(pa.decimal128(precision=7, scale=3)),
    "date": pd.StringDtype(storage="pyarrow"),
    "timestamps": 'datetime64[ns]',
    "float 7:6": pd.StringDtype(storage="pyarrow"),
}

with open("data_dictionary.json", "r") as f:
    data_dict: dict = json.load(f)
    data_dict = {
        k: {key: pandas_mappings[val] for key, val in v.items()}
        for k, v in data_dict.items()
    }


# Process each file in the tmp directory
for f in Path("unzip").iterdir():
    filename = f.stem
    col_types = data_dict[filename]
    if f.exists():
        # Files are txt files with '|' separation
        df = pd.read_csv(f, sep="|", engine="pyarrow", dtype=col_types, on_bad_lines='skip', na_values=[''])

        # Construct the output Parquet file path
        new_file_name = Path(f).relative_to("unzip").with_suffix(".parquet")
        parquet_path = os.path.join("brick", new_file_name)

        # Write Parquet file
        table = pa.Table.from_pandas(df)
        pq.write_table(table, parquet_path)
