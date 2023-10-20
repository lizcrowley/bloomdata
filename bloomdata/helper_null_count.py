import pandas as pd
import numpy as np

df = pd.DataFrame(np.array([[5, 8, np.nan], [20, np.nan, np.nan], [np.nan, np.nan, 11]]),
columns = ['A', 'B', 'C'])

def null_count(df):
    return df.isna().sum().sum()

if __name__ == "__main__":
    print(null_count(df))