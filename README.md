NHL Fatigue Analysis: Independent Project

To what extent do back-to-back games change NHL team performance, after controlling for team strength, home ice advantage, opponent rest, and goalie quality?

\## Hypothesis

&#x09;Hypothesis 1: Back-to-back games lower a team's adjusted performance.

*Adjusted performance will be measured as expected goals share (or goal differential), adjusted for the controls above.*

&#x09;Hypothesis 2: Among back-to-back games the effect of hypothesis 1 is greatest for situations where both games are away, then where the first game is home and the second is away, then where both games are home, then where the first game is away and the second is home.

\*\*Summary\*\*

&#x09;Back-to-back games lowered a team's expected-goals share by about 2.2 percentage points after controlling for home ice, team strength, and opponent rest (Hypothesis 1 supported). The effect did not clearly differ by home/away pattern (Hypothesis 2 not supported). The effect is consistent across seasons but small relative to game-to-game noise.

&#x09;The results from data analysis support my first hypothesis. After controlling for home ice, both teams' pre-game strength (season-to-date xG share), and whether the opponent was also on a back-to-back, teams playing on the second day of a back-to-back had an xG share 2.2 percentage points lower. For example, a team that would normally sit at 50% dropped to about 47.8%. This data was looked at with a 95% confidence interval, meaning the likely range was from 1.6 to 2.7 points, so the plausible effect is entirely below zero. This used 9154 team-games from 2022 to 2025.

&#x09;The results from data analysis did not support my second hypothesis. I predicted that the back-to-back effects would differ depending on where the two games were played, with the biggest drop for two road games in a row. This relationship was speculated from access to team recovery technology however, it was not reflected in the outcome of my analysis. All four patterns showed a similar drop of about 1.6 to 2.7 points, and they weren't in the order I predicted. A statistical test couldn't show that the four patterns differ from each other due to the resulting p value (0.34) making the data statistically insignificant. Each pattern only has 212 to 730 games, so a small correlated difference could still be hidden.



&#x09;Limitations: Each game appears twice in the data, so the effective sample is about half the row count. Team strength is estimated from the same outcome, using only earlier games in the season. Schedule exposure is a proxy for fatigue, and no physiological measures were used. Goalie quality and travel distance are not yet in the models.



&#x09;To check that counting each game twice wasn't the driving result, I repeated the analysis using one row per game (from the home teams perspective). A tired home team had an xG share about 1.9 points lower, and a tired visiting team had a home-team xG share about 2.3 points higher, both staying consistent with the main result.



&#x09;I checked whether the results hold across seasons. Based on 2022-2024 alone, a back-to-back was associated with 2.2 points lower xG share; on 2025 alone, 2.0 points lower. When I used a model to fit on 2022-2024 to predict xG share for 2025 games, adding team strength cut prediction error by about 5%, while adding back-to-back status cut it by about 0.4%. The fatigue effect is consistent but small relative to the noise in a single game.



\## Data:

&#x09;Game-level team data from MoneyPuck, 2022-23 to 2025-26 regular season: 32 teams x 82 games x 4 seasons = 10496 team-game rows. I checked it for duplicates, home/away pairing, goal agreement between the two sides of each game, and dates. I also reconciled 2025 goals and shootout results against a secondary source (see validation log Entry 5).

&#x09;The models use 9,154 of the 10,496 team-games. Rows are excluded when the team’s or opponent’s pre-game strength is not yet defined (fewer than 10 earlier games that season) or when rest days are unavailable (first game of a season).

Source:

&#x09;MoneyPuck.com game-level data (https://moneypuck.com/data.htm). Data are not redistributed in this repository.

\## Method:

&#x09;Outcome is expected goal share = xG for / (xG for + xG against). For each team-game I built rest days, back-to-back flag, opponent rest, and team and opponent strength (season-to-date average xG share, using only earlier games). I fit OLS regressions with standard errors clustered by team and tested H1 and H2 with Wald tests.

\## Results:

!\[Rest days vs xG share](results/rest\_by\_xg\_share.png)

\### H1 (back-to-backs lower performance): 

&#x09;Supported. A team on the second night had a xG share 0.0215 lower (2.2 percentage points), 95% confidence interval (-0.027, -0.016), p < 0.001, after controlling for home ice, own strength, opponent strength, and opponent rest. The opponent being on a back-to-back raised xG share by 0.0215 (CI \[0.015, 0.028])

\### H2: 

&#x09;Not supported. I predicted the effect would be largest for away-then-away back-to-backs, then home-then-away, then home-then-home, then away-then-home. The point estimates (xG share points lower than a game without a back-to-back) were home-then-away 2.8, away-then-away 2.1, away-then-home 2.0, and home-then-home 1.7. The order differs from my prediction.

&#x09;Additionally, the Wald test could not distinguish the four patterns (p = 0.34), so there is no evidence the effect differs by home/away pattern. Comparisons between patterns with the same second-game location also found no difference (away-then-away vs home-then-away: p = 0.19; home-then-home vs away-then-home: p = 0.72). Each pattern has only 212 to 730 games (away-to-away: 730, home-to-away: 341, away-to-home: 314, home-to-home: 212), so a small difference could still be hidden.

\## Robustness: 

&#x09;Because each game appears twice (once per team), I repeated the analysis with one row per game from the home team's perspective (4577 games). A tired home team had an xG share about 1.9 points lower (-0.0189, CI \[-0.028, -0.009], p < 0.001), and a tired visiting team raised the home teams xG share by about 2.3 points (0.0227, CI \[0.015, 0.031]). Both are consistent with the main result.

&#x09;The effect was also stable across periods: -0.0217 (CI \[-0.0290, -0.0145]) in 2022-2024 and -0.0203 (CI \[-0.0306, -0.0101]) in 2025

\## Prediction check:

&#x09;I fit models on 2022-2024 and predicted xG share for 2025 games. Adding team strength cut prediction error (RMSE) from 0.11319 to 0.10777, about 5%. Adding back-to-back status lowered it slightly more to 0.10734, about 0.4%. The fatigue effect is consistent but small relative to the noise in a single game.

\## Practical size:

&#x09;about 0.27 xG per game, calculated as 2 x 0.0215 x average total xG per game (\~6.3).

\## Limitations:

&#x09;Team strength is built from the same outcome I'm modeling

&#x09;Rest days are a proxy for fatigue, not a physiological measure

&#x09;Goalie quality and travel distance are not yet in the models

&#x09;Shootout games are scored as ties in the MoneyPuck goal counts

\## Future Work:

&#x09;

\## How to Reproduce:

&#x09;Run the scripts in src/ in order, from 01 to 04, after downloading the MoneyPuck game level file into data/.

