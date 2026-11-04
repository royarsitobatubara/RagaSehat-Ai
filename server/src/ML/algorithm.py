import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def train_rf_model(X_train: pd.DataFrame, y_train: pd.Series, n_estimators: int = 100, max_depth: int = 5) -> RandomForestClassifier:
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=42
    )
    model.fit(X_train, y_train)
    return model

def train_knn_model(X_train: pd.DataFrame, y_train: pd.DataFrame, n_neighbors: int=5, p: int=2) -> Pipeline:
    knn_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('knn', KNeighborsClassifier(n_neighbors=n_neighbors , metric='minkowski' , p=p))
    ])
    knn_pipeline.fit(X_train, y_train)
    return knn_pipeline