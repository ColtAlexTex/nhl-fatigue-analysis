import pandas as pd

g = pd.read_csv("data/games_clean.csv", parse_dates=["date"])
g = g.sort_values(["season", "team", "date"]).reset_index(drop=True)

# Rest days since the team's previous game (0 = played the day before)
g["prev_date"] = g.groupby(["season", "team"])["date"].shift(1)
g["rest_days"] = (g["date"] - g["prev_date"]).dt.days - 1
g["b2b"] = (g["rest_days"] == 0).astype(int)

# Where the previous game was played, then the back-to-back pattern
g["prev_loc"] = g.groupby(["season", "team"])["home_or_away"].shift(1)
g["b2b_type"] = None
m = g["b2b"] == 1
g.loc[m, "b2b_type"] = g.loc[m, "prev_loc"] + ">" + g.loc[m, "home_or_away"]

# Opponent's rest in the same game
opp = g[["gameId", "team", "rest_days", "b2b"]].rename(
    columns={"team": "opposingTeam", "rest_days": "opp_rest_days", "b2b": "opp_b2b"})
g = g.merge(opp, on=["gameId", "opposingTeam"], how="left")

# Outcomes
g["xg_share"] = g["xGoalsFor"] / (g["xGoalsFor"] + g["xGoalsAgainst"])
g["goal_diff"] = g["goalsFor"] - g["goalsAgainst"]

# First look (each team's first game of a season has no rest value)
d = g.dropna(subset=["rest_days"])
print("rows:", len(g), "| rows with a rest value:", len(d))
print(d["rest_days"].value_counts().sort_index().head(8))
print(d["b2b"].value_counts())
print(d["b2b_type"].value_counts())
print(d.groupby("b2b")[["xg_share", "goal_diff"]].mean())

g.to_csv("data/games_features.csv", index=False)