import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_rf_model(X_train: pd.DataFrame, y_train: pd.Series, n_estimators: int = 100, max_depth: int = 5) -> RandomForestClassifier:
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=42
    )
    
    model.fit(X_train, y_train)
    return model