raw_data = [
    {"employee": "Kim", "salary": "70000", "years": 5},
    {"employee": "Lee", "salary": None, "years": "3"},
    {"employee": "", "salary": "ERR", "years": 10},
    {"employee": "Pat", "salary": "85000", "years": "N/A"}
]

import pandas as pd
import numpy as np

def data_cleaner(raw_data: list[dict]) -> list:
    df = pd.DataFrame(raw_data)

    df.replace("", np.nan,  inplace=True)
    df[df.columns.difference(["employee"])] = df[df.columns.difference(["employee"])].apply(pd.to_numeric, errors="coerce")

    return {
        "cleaned_df": df
    }

def main():
    rs = data_cleaner(raw_data)
    print(rs["cleaned_df"])

if __name__ == "__main__":
    main()