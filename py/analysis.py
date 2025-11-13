import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="fituser",
    password="fitpass123!",
    database="fighting_fit"
)

# Load all fights
df = pd.read_sql("SELECT * FROM fights", conn)

print(df.head())
print(df.info())
