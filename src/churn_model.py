from sklearn.linear_model import LogisticRegression

def train_churn_model(X, y):
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    return model
