import pandas as pd

g = pd.read_csv("data/games_clean.csv")
g = g[g["season"] == 2025]

mine = g.groupby("team")[["goalsFor", "goalsAgainst"]].sum()
tied = g[g["goalsFor"] == g["goalsAgainst"]].groupby("team").size()
mine["tied_games"] = tied.reindex(mine.index).fillna(0).astype(int)

off = pd.read_csv("data/official_standings_hockey_reference.csv")
off = off.rename(columns={off.columns[1]: "name"})
off["name"] = off["name"].str.replace("*", "", regex=False).str.strip()

names = {
    "Anaheim Ducks": "ANA", "Boston Bruins": "BOS", "Buffalo Sabres": "BUF",
    "Calgary Flames": "CGY", "Carolina Hurricanes": "CAR", "Chicago Blackhawks": "CHI",
    "Colorado Avalanche": "COL", "Columbus Blue Jackets": "CBJ", "Dallas Stars": "DAL",
    "Detroit Red Wings": "DET", "Edmonton Oilers": "EDM", "Florida Panthers": "FLA",
    "Los Angeles Kings": "LAK", "Minnesota Wild": "MIN", "Montreal Canadiens": "MTL",
    "Nashville Predators": "NSH", "New Jersey Devils": "NJD", "New York Islanders": "NYI",
    "New York Rangers": "NYR", "Ottawa Senators": "OTT", "Philadelphia Flyers": "PHI",
    "Pittsburgh Penguins": "PIT", "San Jose Sharks": "SJS", "Seattle Kraken": "SEA",
    "St. Louis Blues": "STL", "Tampa Bay Lightning": "TBL", "Toronto Maple Leafs": "TOR",
    "Utah Mammoth": "UTA", "Vancouver Canucks": "VAN", "Vegas Golden Knights": "VGK",
    "Washington Capitals": "WSH", "Winnipeg Jets": "WPG",
}
off["team"] = off["name"].map(names)
print("Names that did not match:", off[off["team"].isna()]["name"].tolist())
off = off.set_index("team")[["GF", "GA", "SOW", "SOL"]]

c = mine.join(off, how="outer")
c["gf_diff"] = c["GF"] - c["goalsFor"]
c["ga_diff"] = c["GA"] - c["goalsAgainst"]
c["so_diff"] = c["SOW"] + c["SOL"] - c["tied_games"]

print(c[["goalsFor", "GF", "gf_diff", "goalsAgainst", "GA", "ga_diff",
         "tied_games", "SOW", "SOL", "so_diff"]])
print("Teams with goals-for differences:", (c["gf_diff"] != 0).sum())
print("Teams with goals-against differences:", (c["ga_diff"] != 0).sum())
print("Teams where SOW + SOL differs from tied games:", (c["so_diff"] != 0).sum())
print("League SOW total:", c["SOW"].sum(), "| SOL total:", c["SOL"].sum())