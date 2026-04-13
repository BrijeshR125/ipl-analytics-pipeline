import sqlite3
import pandas as pd


# creating database connection
try:
    conn = sqlite3.connect('ipl.db')
    print("Database connected successfully!")
except sqlite3.OperationalError as e:
    print(f"Error connecting to database: {e}")
    exit()
except Exception as e:
    print(f"Unexpected error: {e}")
    exit()

# Query 1 - Top 5 teams by wins
try:
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

except pd.io.sql.DatabaseError as e:
    print(f"Error running Query 1: {e}")


# Query 2 - Top 5 batsmen
try:
    print("\n=== Top 5 Batsmen by Runs ===")
    q2 = pd.read_sql("""
        SELECT batter, SUM(batsman_runs) as total_runs
        FROM deliveries
        GROUP BY batter
        ORDER BY total_runs DESC
        LIMIT 5
    """, conn)
    print(q2)
except pd.io.sql.DatabaseError as e:
    print(f"Error running Query 2: {e}")

    
    # Query 3 - Toss decision analysis
try:
    print("\n=== Toss Decision - Bat or Field? ===")
    q3 = pd.read_sql("""
        SELECT toss_decision, COUNT(*) as times_chosen
        FROM matches
        GROUP BY toss_decision
    """, conn)
    print(q3)

except pd.io.sql.DatabaseError as e:
    print(f"Error running Query 3: {e}")


# Query 4 - Most productive venues
try:
    print("\n=== Top 5 Venues ===")
    q4 = pd.read_sql("""
        SELECT venue, COUNT(*) as matches_hosted
        FROM matches
        GROUP BY venue
        ORDER BY matches_hosted DESC
        LIMIT 5
    """, conn)
    print(q4)
except pd.io.sql.DatabaseError as e:
    print(f"Error running Query 4: {e}")


finally:
    if 'conn' in locals() and conn:
        conn.close()
        print("\nDatabase connection closed.")