import pandas as pd

# Load dataset
df = pd.read_csv('../data/ufc-master.csv')

# Preview first rows
print(df.head(10))

# Show columns
print("\nColumns:\n", df.columns)

# Show info
print("\nData Info:")
print(df.info())
