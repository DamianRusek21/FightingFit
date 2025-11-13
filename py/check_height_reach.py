import pandas as pd

# Load the CSV
df = pd.read_csv(r"D:\7Projects\fighting_fit\data\ufc-master.csv")

# Print all columns that contain 'Height'
print("Height columns:")
for col in df.columns:
    if "Height" in col:
        print(col)

# Print all columns that contain 'Reach'
print("\nReach columns:")
for col in df.columns:
    if "Reach" in col:
        print(col)
