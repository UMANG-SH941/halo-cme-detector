# Placeholder for ML model if added later
# Plan: Random Forest on engineered features

def train_model(X, y):
    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier()
    model.fit(X, y)
    return model
