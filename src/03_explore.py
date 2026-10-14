# Explore xG share by rest days and back-to-back pattern; save the plot.
import pandas as pd
import matplotlib.pyplot as plt

g = pd.read_csv("data/games_features.csv", parse_dates=["date"])
d = g.dropna(subset=["rest_days"]).copy()

# Long rest gaps (breaks)
print(d["rest_days"].value_counts().sort_index().tail(8))

# Share of games that are home vs away, for back-to-back and other games
print(d.groupby("b2b")["home_or_away"].value_counts(normalize=True).round(3))

# xG share by home/away and back-to-back
print(d.groupby(["home_or_away", "b2b"])["xg_share"].agg(["mean", "count"]).round(4))

# xG share by back-to-back pattern
print(d.groupby("b2b_type")["xg_share"].agg(["mean", "count"]).round(4))

# xG share by rest days (3 or more grouped together)
d["rest_cat"] = d["rest_days"].clip(upper=3).astype(int)
s = d.groupby("rest_cat")["xg_share"].agg(["mean", "std", "count"])
s["se"] = s["std"] / s["count"] ** 0.5
print(s.round(4))

plt.errorbar(s.index, s["mean"], yerr=1.96 * s["se"], fmt="o-", capsize=4)
plt.xticks([0, 1, 2, 3], ["0 (b2b)", "1", "2", "3+"])
plt.xlabel("Rest days before the game")
plt.ylabel("xG share")
plt.title("xG share by rest days (95% CI)")
plt.savefig("results/rest_by_xg_share.png", dpi=150, bbox_inches="tight")