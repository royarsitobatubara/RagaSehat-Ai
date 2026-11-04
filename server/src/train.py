import os
import sys
import pandas as pd
from typing import Optional

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SERVER_DIR  = os.path.dirname(CURRENT_DIR)
if SERVER_DIR not in sys.path:
    sys.path.append(SERVER_DIR)

from src.ML import detect_duplicated, drop_duplicated, detect_null, detect_outliers, cap_outliers

PATH_DATA_HEART = os.path.join(SERVER_DIR, "data", "heart.csv")
PATH_DATA_DIABETES = os.path.join(SERVER_DIR, "data", "diabetes.csv")
PATH_MODEL = os.path.join(SERVER_DIR, "model")

def read_data(path_data:str) -> Optional[pd.DataFrame]:
    print("Proses pengambilan data...")
    if not os.path.exists(path_data):
        print(f"File data tidak ditemukan {path_data}")
        return None
    data = pd.read_csv(path_data)
    return data

def train_model_heart():
    df = read_data(PATH_DATA_HEART)
    if df is None:
        print("[HEART] Proses training dibatalkan karena dataset tidak ditemukan.")
        return
    detect_duplicated(df=df)
    df_clean = drop_duplicated(df=df)
    detect_duplicated(df=df_clean)
    detect_null(df=df_clean)
    detect_outliers(df=df_clean, columns=df_clean.columns)
    df_clean = cap_outliers(df=df_clean, columns=df_clean.columns)
    detect_outliers(df=df_clean, columns=df_clean.columns)
    return

def train_model_diabetes():
    df = read_data(PATH_DATA_DIABETES)
    if df is None:
        print("[DIABETES] Proses training dibatalkan karena dataset tidak ditemukan.")
        return
    detect_duplicated(df=df)
    df_clean = drop_duplicated(df=df)
    detect_duplicated(df=df_clean)
    detect_null(df=df_clean)
    detect_outliers(df=df_clean, columns=df_clean.columns)
    df_clean = cap_outliers(df=df_clean, columns=df_clean.columns)
    detect_outliers(df=df_clean, columns=df_clean.columns)
    return

if __name__ == "__main__":
    train_model_heart()
    train_model_diabetes()