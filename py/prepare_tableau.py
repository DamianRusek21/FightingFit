import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="fituser",
    password="fitpass123!",
    database="fighting_fit"
)

# Load data
df = pd.read_sql("SELECT * FROM fights", conn)

# Create useful derived columns
df['height_diff'] = df['red_height_cm'] - df['blue_height_cm']
df['reach_diff'] = df['red_reach_cm'] - df['blue_reach_cm']
df['avg_td_diff'] = df['red_avg_td_landed'] - df['blue_avg_td_landed']

# Optional: encode winner as 0/1 for analysis
df['red_win'] = df['winner'].apply(lambda x: 1 if x.lower() == 'red' else 0)

# Save to CSV for Tableau
df.to_csv("../data/ufc_tableau_ready.csv", index=False)
print("✅ Tableau-ready CSV saved!")
