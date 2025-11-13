import mysql.connector
import pandas as pd
import numpy as np

# ---- 1. Connect to MySQL ----
conn = mysql.connector.connect(
    host="localhost",
    user="fituser",
    password="fitpass123!",
    database="fighting_fit"
)
cursor = conn.cursor()

# ---- 2. Load CSV ----
file_path = r"D:\7Projects\fighting_fit\data\ufc-master.csv"
df = pd.read_csv(file_path)

# ---- 3. Replace NaN with None ----
df = df.replace({np.nan: None})

# ---- 4. Prepare insert statement ----
insert_sql = """
INSERT INTO fights (
    event_date, event_name, weight_class, winner,
    red_fighter, blue_fighter, red_height_cm, blue_height_cm,
    red_reach_cm, blue_reach_cm, red_age, blue_age,
    red_odds, blue_odds, red_avg_td_landed, blue_avg_td_landed
)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

# ---- 5. Build records ----
records = []

for _, row in df.iterrows():
    records.append((
        row.get("Date"),
        row.get("Event"),
        row.get("WeightClass"),
        row.get("Winner"),
        row.get("RedFighter"),
        row.get("BlueFighter"),
        float(row["RedHeightCms"]) if row["RedHeightCms"] is not None else None,
        float(row["BlueHeightCms"]) if row["BlueHeightCms"] is not None else None,
        float(row["RedReachCms"]) if row["RedReachCms"] is not None else None,
        float(row["BlueReachCms"]) if row["BlueReachCms"] is not None else None,
        int(row["RedAge"]) if row["RedAge"] is not None else None,
        int(row["BlueAge"]) if row["BlueAge"] is not None else None,
        float(row["RedOdds"]) if row["RedOdds"] is not None else None,
        float(row["BlueOdds"]) if row["BlueOdds"] is not None else None,
        float(row["RedAvgTDLanded"]) if row["RedAvgTDLanded"] is not None else None,
        float(row["BlueAvgTDLanded"]) if row["BlueAvgTDLanded"] is not None else None
    ))

# ---- 6. Execute insert ----
cursor.executemany(insert_sql, records)
conn.commit()

print(f"✅ Loaded {cursor.rowcount} fights into MySQL successfully.")

cursor.close()
conn.close()
