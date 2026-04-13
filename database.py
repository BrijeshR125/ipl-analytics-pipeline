import pandas as pd
import sqlite3

# Loading the data
try:
    matches = pd.read_csv('matches.csv')
    deliveries = pd.read_csv('deliveries.csv')
except FileNotFoundError as e:
    print(f"Error: {e}. Please check if CSV files exist.")
    exit()
except Exception as e:
    print(f"Error loading CSV files: {e}")
    exit()

try:
    # Creating the database
    conn = sqlite3.connect('ipl.db')
    matches.to_sql('matches', conn, if_exists='replace', index=False)
    deliveries.to_sql('deliveries', conn, if_exists='replace', index=False)

    print("Data loaded successfully!")
    print("Matches rows:", pd.read_sql("SELECT COUNT(*) as count FROM matches", conn)['count'][0])
    print("Deliveries rows:", pd.read_sql("SELECT COUNT(*) as count FROM deliveries", conn)['count'][0])

except sqlite3.OperationalError as e:
    print(f"Database operation error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    if 'conn' in locals() and conn:
        conn.close()
        print("Database connection closed.")