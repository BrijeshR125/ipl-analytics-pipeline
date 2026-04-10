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