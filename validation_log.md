Validation Log



Data source: MoneyPuck.com game-level file (`all\_teams.csv`, saved as `data/games\_all.csv`)

Date checked: October 12, 2026

Raw file: 233,080 rows x 111 columns. Each team-game appears 5 times, once per game situation (all, 5on5, 5on4, 4on5, other): 5 x 46,616 = 233,080.

Working table: situation = "all" and playoffGame = 0 (one row per team per regular-season game), then restricted to seasons 2022-2025. The `season` column is the year the season starts, so 2022 means 2022-23.



Entry 1:

Arizona home games, 2011 to 2013 (outside analysis window)

&#x09;I check whether every game has exactly one HOME row and one AWAY row.

&#x09;I found that 106 games (212 rows) have two AWAY rows and no HOME row. They are 41 games in 2011, 24 games in 2012, and 41 games in 2014. In the rows I looked at, the affected team's row lists ARI as its own opponent, while the opponent's row correctly shows ARI as the opposing team and AWAY.

&#x09;I tested to see if the explanation for this was a team-code change, but ruled that out because ARI is the team code in 2010, 2011, 2012, 2013, and 2014. The idea that the team lacked an arena or relocated was also unsupported, because the opponents row treated these as ARI home games. That points to a labeling erroring the team's own row, but this is an inference and I haven't confirmed it.

&#x09;Cause is unknown

&#x09;I still need to verify how many affected games involve ARI per season

&#x09;The action I made on the issue was excluding these games by the season window I chose. If this window is extended, ARI's row would need correcting from the other row of the same gameId, or the games would be excluded.

&#x09;There is no impact for the data range I selected to analyze (2022 to 2025).



Entry 2:

Missing games from 2008 and 2009 (outside analysis window)

&#x09;I checked rows per season compared with expected teams multiplied by the 82 games in a season.

&#x09;I found that 2008 has 2454 rows, compared to the 2460 expected. 2009 has 2458 rows, compared to the expected 2460 expected. Meaning that 2008 was missing 3 games and 2009 was missing 1 game. Other full seasons matched exactly.

&#x09;I did not investigate the cause. The games may be missing from the source or dropped by my filters.

&#x09;No action needed since both seasons are outside the analysis window.



Entry 3:

Team code changed from ARI to UTA

&#x09;I checked team codes by season for 2023, 2024, and 2025.

&#x09;I found that the franchise is ARI in 2022 and 2023, and UTA in 2024 and 2025. The two codes never appear together in the same season, and each season has 32 teams.

&#x09;*Background: according to Wikipedia's Mullet Arena page (accessed October 12, 2026), the Arizona Coyotes played their home games at Mullet Arena in Tempe, Arizona from 2022 to 2024, so both ARI seasons in my window were played there. The same page states that after the 2023-24 season the Coyotes suspended operations and many of their assets moved to Utah to form a new team, which it describes as technically an expansion team. I am treating ARI and UTA as two separate teams because they have different codes and play in different arenas for the purposes of this analysis.*

&#x09;There will be no observed consequences to my analysis of within-seasons calculations (rest days, back-to-backs, season-to-date strength). Anything that uses past season's history would leave Utah's first seasons without history so I am using season-to-date strength instead. Travel distances need separate arena locations for ARI and UTA.

&#x09;I will keep ARI and UTA as separate team labels. When I build the arena file, ARI will use Mullet Arena and UTA will use the Delta Center, with primary and secondary sources recorded for each.

&#x09;I still need to confirm that these are the arenas used for the entirety of the games played in my data window, and collect home arenas for the other 31 teams.





Entry 4: 

Window choice; analyzing the 2022 to 2025 seasons.

&#x09;2022, 2023, 2024, and 2025 each have 2624 rows, accounting for all 32 teams having 82 games. Earlier seasons have irregular schedules; 2012 was a lockout year with 48 games, 2019 was cut short by COVID, 20220 was a 56-game season with a division only schedule, and 2021 was a full length season but had COVID postponements that would distort rest day calculations. 2017 and 2018 had 31 teams, so they aren't comparable. The labeling error from Entry 1 is outside this window. The 2026-27 NHL season is in progress and only contains 172 rows, so it is excluded.



Entry 5:

Check against official standings for all 32 teams (2025 season)

&#x09;I compared each team's season goals for and against in my cleaned data with the Hockey Reference standings, which I copied into my spreadsheet by hand. MoneyPuck goals exclude shootout goals, so I compared against in-play goals. NHL games cannot end tied, so a game with equal goals in MoneyPuck is a shootout game. I checked that each team's shootout wins plus shootout losses equals it's tied games

&#x09;Goals for differed for 0 out of the 32 teams, and goals against differed for 0 of the 32. Shootout wins plus losses equaled tied games for all 32 teams, which equaled a league total of 119 wins and 119 losses.

&#x09;I did not check games played at neutral sites.





























