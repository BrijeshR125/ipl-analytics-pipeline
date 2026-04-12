import pandas as pd

# CSV file load
df = pd.read_csv('matches.csv')

# Basic exploration
print("Total rows:", df.shape[0])
print("Total columns:", df.shape[1])
print("---")
print(df.head())
print("---")
print(df.columns)


# 4. Kaun sa venue sabse zyada matches host karta hai?
print("\nTop 5 Venues:")
print(df['venue'].value_counts().head(5))

# 5. Toss jeetne wale ne match bhi jeeta kitni baar?
toss_match_win = df[df['toss_winner'] == df['winner']]
percentage = round(len(toss_match_win) / len(df) * 100, 2)
print("\nToss winner = Match winner:", percentage, "%")

# 6. Season wise kitne matches hue?
print("\nMatches per season:")
print(df.groupby('season')['id'].count())

# 7. Loading delevery.csv data
df2 = pd.read_csv('deliveries.csv')

print("Deliveries shape:", df2.shape)
print("---")
print(df2.columns.tolist())
print("---")
print(df2.head())


# Top batsmen by total runs
print("\nTop 10 Batsmen by Runs:")
top_batsmen = df2.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
print(top_batsmen)

# Runs by Virat Kohli
virat = df2[df2['batter'] == 'V Kohli']['batsman_runs'].sum()
print("\nVirat Kohli total runs:", virat)

# Runs by MS Dhoni
dhoni = df2[df2['batter'] == 'MS Dhoni']['batsman_runs'].sum()
print("MS Dhoni total runs:", dhoni)

# Runs by Rohit Sharma
rohit = df2[df2['batter'] == 'RG Sharma']['batsman_runs'].sum()
print("Rohit Sharma total runs:", rohit)

# Top 10 bowlers by wickets
print("\nTop 10 Bowlers by Wickets:")
wickets = df2[df2['is_wicket'] == 1].groupby('bowler')['is_wicket'].count().sort_values(ascending=False).head(10)
print(wickets)

# Most sixes in IPL
print("\nMost Sixes:")
sixes = df2[df2['batsman_runs'] == 6].groupby('batter')['batsman_runs'].count().sort_values(ascending=False).head(10)
print(sixes)