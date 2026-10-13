import pandas as pd
import statsmodels.formula.api as smf

g = pd.read_csv("data/games_features.csv", parse_dates=["date"])
g = g.sort_values(["season", "team", "date"]).reset_index(drop=True)

# Team strength before each game: season-to-date average xG share
# (shift(1) leaves out the current game; min_periods=10 needs 10 earlier games)
g["strength"] = g.groupby(["season", "team"])["xg_share"].transform(
    lambda s: s.shift(1).expanding(min_periods=10).mean())

# Opponent's strength in the same game
opp = g[["gameId", "team", "strength"]].rename(
    columns={"team": "opposingTeam", "strength": "opp_strength"})
g = g.merge(opp, on=["gameId", "opposingTeam"], how="left")

g["home"] = (g["home_or_away"] == "HOME").astype(int)
g["b2b_pattern"] = g["b2b_type"].fillna("none")

# Keep rows that have every variable we need
d = g.dropna(subset=["rest_days", "strength", "opp_strength", "opp_rest_days"]).copy()
d["team_id"] = d["team"].astype("category").cat.codes
print("rows used in models:", len(d))

def fit(formula):
    return smf.ols(formula, data=d).fit(
        cov_type="cluster", cov_kwds={"groups": d["team_id"]})

m1 = fit("xg_share ~ home")
m2 = fit("xg_share ~ home + strength + opp_strength")
m3 = fit("xg_share ~ home + strength + opp_strength + b2b")
m4 = fit("xg_share ~ home + strength + opp_strength + b2b + opp_b2b")
m5 = fit('xg_share ~ home + strength + opp_strength + opp_b2b'
         ' + C(b2b_pattern, Treatment("none"))')

# Compare the back-to-back estimate as controls are added
for name, m in [("m1 home only", m1), ("m2 + strength", m2),
                ("m3 + b2b", m3), ("m4 + opp b2b", m4)]:
    line = f"{name}: R2={m.rsquared:.4f}"
    if "b2b" in m.params:
        lo, hi = m.conf_int().loc["b2b"]
        line += f" | b2b coef={m.params['b2b']:.4f} CI [{lo:.4f}, {hi:.4f}] p={m.pvalues['b2b']:.4f}"
    print(line)

print(m4.summary())
print(m5.summary())

# H2: do the four back-to-back patterns differ from each other?
d["aa"] = (d["b2b_pattern"] == "AWAY>AWAY").astype(int)
d["ah"] = (d["b2b_pattern"] == "AWAY>HOME").astype(int)
d["ha"] = (d["b2b_pattern"] == "HOME>AWAY").astype(int)
d["hh"] = (d["b2b_pattern"] == "HOME>HOME").astype(int)

m6 = fit("xg_share ~ home + strength + opp_strength + opp_b2b + aa + ah + ha + hh")
print("All four patterns equal:")
print(m6.wald_test("aa = ah, aa = ha, aa = hh", scalar=True))
print("AWAY>AWAY vs HOME>AWAY:")
print(m6.wald_test("aa = ha", scalar=True))
print("HOME>HOME vs AWAY>HOME:")
print(m6.wald_test("hh = ah", scalar=True))