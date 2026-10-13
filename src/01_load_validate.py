import pandas as pd

# Load the MoneyPuck file
df = pd.read_csv("data/games_all.csv")

# One row per team per game: all situations, regular season only
g = df[(df["situation"] == "all") & (df["playoffGame"] == 0)].copy()

# Modeling window: seasons 2022-2025
g = g[g["season"].between(2022, 2025)].copy()

# Turn 20221007 into a real date
g["date"] = pd.to_datetime(g["gameDate"].astype(str), format="%Y%m%d")
g = g.sort_values(["team", "date"]).reset_index(drop=True)

# C1: row counts
print("C1 rows per season:")
print(g.groupby("season").size())
print("C1 rows per game (should all be 2):")
print(g.groupby("gameId").size().value_counts())

# C2: duplicates and missing values
print("C2 duplicate team-games:", g.duplicated(subset=["team", "gameId"]).sum())
cols = ["season", "date", "team", "opposingTeam", "home_or_away",
        "goalsFor", "goalsAgainst", "xGoalsFor", "xGoalsAgainst"]
print("C2 missing values:")
print(g[cols].isna().sum())

# C3: does each team's row agree with its opponent's row?
m = g.merge(g, on="gameId", suffixes=("", "_o"))
m = m[m["team"] != m["team_o"]]
print("C3 paired rows (should be", len(g), "):", len(m))
print("C3 goal mismatches:", (m["goalsFor"] != m["goalsAgainst_o"]).sum())
print("C3 largest xG gap:", (m["xGoalsFor"] - m["xGoalsAgainst_o"]).abs().max())
print("C3 games without one HOME and one AWAY:",
      (g.groupby("gameId")["home_or_away"].nunique() != 2).sum())

# C4: dates
print("C4 date range:", g["date"].min(), "to", g["date"].max())
print("C4 team plays twice on the same date:", g.duplicated(subset=["team", "date"]).sum())

# Save the cleaned table for the next step
g.to_csv("data/games_clean.csv", index=False)
print("saved", g.shape)