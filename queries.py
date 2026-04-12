import sqlite3
import pandas as pd

conn = sqlite3.connect('ipl.db')

# Query 1 - Top 5 teams by wins
print("=== Top 5 Teams by Wins ===")
q1 = pd.read_sql("""
    SELECT winner, COUNT(*) as total_wins 
    FROM matches 
    WHERE winner IS NOT NULL
    GROUP BY winner 
    ORDER BY total_wins DESC 
    LIMIT 5
""", conn)
print(q1)

# Query 2 - Top 5 batsmen
print("\n=== Top 5 Batsmen by Runs ===")
q2 = pd.read_sql("""
    SELECT batter, SUM(batsman_runs) as total_runs
    FROM deliveries
    GROUP BY batter
    ORDER BY total_runs DESC
    LIMIT 5
""", conn)
print(q2)

# Query 3 - Toss decision analysis
print("\n=== Toss Decision - Bat or Field? ===")
q3 = pd.read_sql("""
    SELECT toss_decision, COUNT(*) as times_chosen
    FROM matches
    GROUP BY toss_decision
""", conn)
print(q3)

# Query 4 - Most productive venues
print("\n=== Top 5 Venues ===")
q4 = pd.read_sql("""
    SELECT venue, COUNT(*) as matches_hosted
    FROM matches
    GROUP BY venue
    ORDER BY matches_hosted DESC
    LIMIT 5
""", conn)
print(q4)

conn.close()