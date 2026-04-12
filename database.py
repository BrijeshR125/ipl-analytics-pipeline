import pandas as pd
import sqlite3

# Creating the database
conn = sqlite3.connect('ipl.db')

# Loading the data
matches = pd.read_csv('matches.csv')
deliveries = pd.read_csv('deliveries.csv')

matches.to_sql('matches', conn, if_exists='replace', index=False)
deliveries.to_sql('deliveries', conn, if_exists='replace', index=False)

print("Data loaded successfully!")
print("Matches rows:", pd.read_sql("SELECT COUNT(*) as count FROM matches", conn)['count'][0])
print("Deliveries rows:", pd.read_sql("SELECT COUNT(*) as count FROM deliveries", conn)['count'][0])

conn.close()