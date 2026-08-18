raw_data = [
    {"account": "X1", "amount": "1000", "fee": "25"},
    {"account": "X2", "amount": None, "fee": "ERR"},
    {"account": "", "amount": "N/A", "fee": 15},
    {"account": "X4", "amount": 2000, "fee": None}
]

import pandas as pd
import numpy as np

def data_cleaner(raw_data: list[dict]) -> list:

    df = pd.DataFrame(raw_data)
    df.replace("", np.nan,inplace=True)
    non_account_col = df.columns.difference(["account"])
    df[non_account_col] = df[non_account_col].apply(
        pd.to_numeric,
        errors="coerce"
    )

    print(df)


data_cleaner(raw_data)