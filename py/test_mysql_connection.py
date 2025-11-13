import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="fituser",             # 👈 new user
        password="fitpass123!",     # 👈 new password
        database="fighting_fit"     # 👈 same database you just created
    )

    if conn.is_connected():
        print("✅ Successfully connected to MySQL database as fituser!")
    conn.close()

except mysql.connector.Error as err:
    print(f"❌ Connection failed: {err}")
