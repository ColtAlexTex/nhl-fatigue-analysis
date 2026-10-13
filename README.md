NHL Fatigue Analysis: Independent Project

To what extent do back-to-back games, rest gaps, and travel change NHL team performance, after controlling for team strength, home ice advantage, opponent rest, and goalie quality?



&#x09;Hypothesis 1: Back-to-back games lower a team's adjusted performance.

*Adjusted performance will be measured as expected goals share (or goal differential), adjusted for the controls above.*

&#x09;Hypothesis 2: Among back-to-back games the effect of hypothesis 1 is greatest for situations where both games are away, then where the first game is home and the second is away, then where both games are home, then where the first game is away and the second is home.



&#x09;The results from data analysis support my first hypothesis. After controlling for home ice, both teams' pre-game strength (season-to-date xG share), and whether the opponent was also on a back-to-back, teams playing on the second day of a back-to-back had an xG share \~2.2 percentage points lower. For example, a team that would normally sit at 50% dropped to about 47.8%. This data was looked at with a 95% confidence interval, meaning the likely range was from 1.7 to 2.8 points, meaning the correlation is unlikely to be flawed. This used 9154 team-games from 2022 to 2025.



&#x09;The results from data analysis did not support my second hypothesis. I predicted that the back-to-back effects would differ depending on where the two home games were played, with the biggest drop for two road games in a row. This relationship was speculated from access to team recovery technology however, it was not reflected in the outcome of my analysis. All four patterns showed a similar drop of about 1.7 to 2.8 points, and they weren't in the order I predicted. A statistical test couldn't show that the four patterns differ from each other due to the resulting p value (0.34) being significant enough to discourage a definitive correlation. Each pattern only has 212 to 730 games, so a small correlated difference could still be hidden.



&#x09;Limitations: Each game appears twice in the data, so the effective sample is about half the row count. Team strength is estimated from the same outcome, using only earlier games in the season. Schedule exposure is a proxy for fatigue, and no physiological measures where used. Goalie quality and travel distance are not yet in the models.



&#x09;To check that counting each game twice wasn't the driving result, I repeated the analysis using one row per game (from the home teams perspective). A tired home team had a xG share about 1.9 points lower, and a tired visiting team had a home-team xG share about 2.3 points higher, both staying consistent with the main result.



&#x09;I checked whether the results hold across seasons. Based on 2022-2024 alone, a back-to-back was associated with 2.2 points lower xG share; on 2025 alone, 2.0 points lower. When I used a model to fit on 2022-2024 to predict xG share for 2025 games, adding team strength cut prediction error by about 5%, while adding back-to-back status cut it by about 0.4%. The fatigue effect is consistent but small relative to the noise in a single game.

