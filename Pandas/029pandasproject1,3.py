raw_data = [
    {"student": "Ana", "math": "88", "science": 91},
    {"student": "Ben", "math": None, "science": "ERR"},
    {"student": "Cal", "math": "N/A", "science": 85},
    {"student": "", "math": 77, "science": 80}
]

import numpy as np
import pandas as pd

def data_cleaner(raw_data: list[dict]) -> dict:
    df = pd.DataFrame(raw_data)

    df = df.replace("", np.nan)
    non_stu_col = df.columns.difference(["student"])
    df[non_stu_col] = df[non_stu_col].apply(
        pd.to_numeric, errors="coerce"
    )

    return {
        "cleaned_df": df
    }



rs = data_cleaner(raw_data)
print(f"Cleaned Data Frame:\n{rs["cleaned_df"]}")