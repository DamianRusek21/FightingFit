import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load cleaned dataset
df = pd.read_csv("D:/7Projects/fighting_fit/data/ufc_tableau_ready.csv")

# Create target
df["red_win"] = (df["winner"] == "Red").astype(int)

# Feature engineering
df["height_diff"] = df["red_height_cm"] - df["blue_height_cm"]
df["reach_diff"] = df["red_reach_cm"] - df["blue_reach_cm"]
df["age_diff"] = df["red_age"] - df["blue_age"]

features = [
    "height_diff",
    "reach_diff",
    "age_diff",
    "red_odds",
    "blue_odds",
    "red_avg_td_landed",
    "blue_avg_td_landed"
]

X = df[features].fillna(0)
y = df["red_win"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train Random Forest
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:\n")
print(classification_report(y_test, predictions))

# Feature importance
importance = pd.Series(
    model.feature_importances_,
    index=features
).sort_values(ascending=False)

print("\nFeature Importance:")
print(importance)
