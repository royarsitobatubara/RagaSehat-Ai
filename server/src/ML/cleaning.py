import pandas as pd
import numpy as np

def detect_duplicated(df: pd.DataFrame):
    print("⌛ Sedang menghitung data duplikat...")
    count = df.duplicated().sum()
    print(f"✅ Duplicate data =  {count}\n")

def drop_duplicated(df: pd.DataFrame):
    print("⌛ Sedang menghapus data duplikat..\n")
    df_clean = df.copy()
    return df_clean.drop_duplicates()

def detect_null(df: pd.DataFrame):
    df_clean = df.copy()
    print(f"Null Data :\n{df_clean.isnull().sum()}\n")
    return 

def detect_outliers(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    summary = []
    for col in columns:
        if col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            # Kurung buka-tutup wajib untuk operator bitwise |
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            
            summary.append({
                'Kolom': col,
                'Batas Bawah': round(lower_bound, 2),
                'Batas Atas': round(upper_bound, 2),
                'Jumlah Outliers': len(outliers)
            })
    print(f"OUTLIERS :\n{pd.DataFrame(summary)}\n")
    return


def cap_outliers(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    df_clean = df.copy()
    for col in columns:
        if col in df_clean.columns:
            Q1 = df_clean[col].quantile(0.25)
            Q3 = df_clean[col].quantile(0.75)
            IQR = Q3 - Q1

            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            df_clean[col] = np.where(
                df_clean[col] > upper_bound, upper_bound,
                np.where(df_clean[col] < lower_bound, lower_bound, df_clean[col])
            )
    print("✅ Berhasil menghapus Outlier\n")
    return df_clean