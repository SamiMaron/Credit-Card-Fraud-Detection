from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from src.preprocess import load_and_clean_data, preprocess_data, balance_data

def train_model(X_train, y_train):
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model

if __name__ == "__main__":
    df = load_and_clean_data("data/creditcard.csv")
    X_train, X_test, y_train, y_test = preprocess_data(df)
    X_train_balanced, y_train_balanced = balance_data(X_train, y_train)
    
    model = train_model(X_train_balanced, y_train_balanced)
    
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))
