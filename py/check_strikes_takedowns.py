import pandas as pd

df = pd.read_csv(r"D:\7Projects\fighting_fit\data\ufc-master.csv")

# Columns related to strikes
print("Strike columns:")
for col in df.columns:
    if "Strike" in col or "SIG" in col:
        print(col)

# Columns related to takedowns
print("\nTakedown columns:")
for col in df.columns:
    if "TD" in col or "Takedown" in col:
        print(col)
