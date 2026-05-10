raw_data = [
    {"sensor": "A1", "temp": "20.5", "humidity": 30},
    {"sensor": "A2", "temp": None, "humidity": "ERR"},
    {"sensor": "A3", "temp": "N/A", "humidity": 45},
    {"sensor": "", "temp": 22.1, "humidity": 40}
]

import pandas as pd
import numpy as np

def data_cleaner(raw_data: list[dict]) -> list:
    
    df = pd.DataFrame(raw_data)

    df = df.replace("", np.nan)
    non_name_col = df.columns.difference(["sensor"])
    df[non_name_col] = df[non_name_col].apply(pd.to_numeric, errors="coerce")

    return {
        "cleaned_df": df
    }

def main():
    rs = data_cleaner(raw_data)
    print(rs["cleaned_df"])

if __name__ == "__main__":
    main()