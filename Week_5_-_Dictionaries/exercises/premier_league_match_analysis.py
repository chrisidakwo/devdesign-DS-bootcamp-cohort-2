# Premier League Gameweek Analysis

# You're a Data Analyst at a sports analytics company (like Opta Sports, Sofascore)
# Your job is to analyze match statistics to provide insights for punters, team managers,
# sports journalists, and fantasy football players.
# You're required to analyze goal-scoring patterns from the latest gameweek.

# Sport analytics companies use exact techniques to power platforms like FPL, betting odds, tactical analysis, etc.

# The Problem
# We have goal data from 10 PL matches in a game week, and are required to:
# 1. Retrieve and display how many goals each team scored
# 2. Find the highest scoring teams and matches
# 3. Calculate goal statistics (average goals per match, most prolific teams)
# 4. Identify teams in good form vs struggling teams

from pprint import pprint

gameweek_matches = [
    {"match_id": 1, "home_team": "Arsenal", "away_team": "Brighton", 
     "home_goals": 3, "away_goals": 0, "venue": "Emirates Stadium"},

    {"match_id": 2, "home_team": "Liverpool", "away_team": "Bournemouth", 
     "home_goals": 4, "away_goals": 1, "venue": "Anfield"},

    {"match_id": 3, "home_team": "Man City", "away_team": "Everton", 
     "home_goals": 2, "away_goals": 1, "venue": "Etihad Stadium"},

    {"match_id": 4, "home_team": "Chelsea", "away_team": "Wolves", 
     "home_goals": 3, "away_goals": 1, "venue": "Stamford Bridge"},

    {"match_id": 5, "home_team": "Newcastle", "away_team": "Fulham", 
     "home_goals": 2, "away_goals": 2, "venue": "St James' Park"},

    {"match_id": 6, "home_team": "Aston Villa", "away_team": "Man United", 
     "home_goals": 1, "away_goals": 2, "venue": "Villa Park"},

    {"match_id": 7, "home_team": "Tottenham", "away_team": "Brentford", 
     "home_goals": 2, "away_goals": 2, "venue": "Tottenham Hotspur Stadium"},

    {"match_id": 8, "home_team": "West Ham", "away_team": "Crystal Palace", 
     "home_goals": 0, "away_goals": 1, "venue": "London Stadium"},

    {"match_id": 9, "home_team": "Nottingham Forest", "away_team": "Sheffield United", 
     "home_goals": 1, "away_goals": 0, "venue": "City Ground"},

    {"match_id": 10, "home_team": "Luton Town", "away_team": "Burnley", 
     "home_goals": 1, "away_goals": 1, "venue": "Kenilworth Road"}
]

print("\nPREMIER LEAGUE GAMEWEEK 18 ANALYSIS")
print("="*60)

# Step 1 - Extract Goals Per Team
# Concept: Process a list of dictionaries to aggregate team statistics

team_goals = {}

for match in gameweek_matches:
    # Extra match data
    home_team = match["home_team"]
    away_team = match["away_team"]
    home_goals = match["home_goals"]
    away_goals = match["away_goals"]

    # Get goals for home team
    team_goals[home_team] = home_goals

    # Get goals for away team
    team_goals[away_team] = away_goals

print("Team Goals:")
pprint(team_goals)
print("")

print("\n========== GOALS SCORED BY TEAM ==========")
for (team, goals) in team_goals.items():
    print(f"    {team}: {goals} goal(s)")

# Step 2a - Highest Scoring Teams
print("\n========== HIGHEST SCORING TEAMS ==========")
goals_threshold = 3

highest_scoring_teams = {}
for (team, goals) in team_goals.items():
    if goals >= goals_threshold:
        highest_scoring_teams[team] = goals

pprint(highest_scoring_teams)

# Step 2b - Highest Scoring Matches
print("\n========== HIGHEST SCORING MATCHES ==========")
match_goals_threshold = 4
highest_scoring_matches = []

for match in gameweek_matches:
    home_goals = match["home_goals"]
    away_goals = match["away_goals"]

    if (home_goals + away_goals) >= match_goals_threshold:
        __match = match.copy()
        del __match["venue"]
        del __match["match_id"]

        highest_scoring_matches.append(__match)

pprint(highest_scoring_matches)

#  TODO: Display the content of `highest_scoring_teams` and `highest_scoring_matches` in a human-readable format, as take-home exercise

# Step 3 - Calculate Match Stats
print("\n========== MATCH STATISTICS ==========")

total_goals = sum(team_goals.values())
avg_goals_per_match = total_goals / len(gameweek_matches)

teams = ", ".join(highest_scoring_teams.keys())

print(f"    Avg Goals Per Game: {avg_goals_per_match}")
print(f"    Top Teams: {", ".join(highest_scoring_teams.keys())}")
print("")
print("="*30)

for match in gameweek_matches:
    home = match["home_team"]
    away = match["away_team"]
    home_goals = match["home_goals"]
    away_goals = match["away_goals"]

    total_match_goals = home_goals + away_goals

    # Display match result
    if home_goals > away_goals:
        result = f"✓ {home} WIN"
    elif away_goals > home_goals:
        result = f"✓ {away} WIN"
    else:
        result = f"🤝 Draw"

    # Determine entertainment rating
    if total_match_goals >= 5:
        entertainment = "🔥 THRILLER"
    elif total_match_goals >= 3:
        entertainment = "🤪 Exciting"
    elif total_match_goals == 0:
        entertainment = "😴 Boring"
    else:
        entertainment = "✓ Decent"
    
    print(f"\n  {home} {home_goals}-{away_goals} {away}")
    print(f"    {result} | {total_match_goals} goals | {entertainment}")
    print(f"    Venue: {match["venue"]}")

# Step 4 - Team Form Classification
print("\n========== TEAM FORM CLASSIFICATION ==========")

# Classifications:
# 1. Excellent form is for teams that score 3+ goals
# 2. Good form is for teams that score 2 goals
# 3. Average form is for teams that score 1 goals
# 4. Poor form is for teams that score 0 goals

# Struggling teams = teams in average and poor form
# Good teams = teams in good and excellent form

excellent_form = {}
good_form = {}
average_form = {}
poor_form = {}

for (__team, __goals) in team_goals.items():
    if __goals >= 3:
        excellent_form[__team] = __goals
    elif __goals == 2:
        good_form[__team] = __goals
    elif __goals == 1:
        average_form[__team] = __goals
    else:
        poor_form[__team] = __goals

print(f"\n EXCELLENT FORM (3+ goals): {len(excellent_form)} teams")
for (team_, goals_) in excellent_form.items():
    print(f"    {team_}: {goals_} goals - Title contenders")

#  TODO: Complete the display for the other classifications as take-home exercise

# Good form: Solid attack
# Average form: Need improvement
# Poor form: Major concern!

# Performance summary
scoring_teams = len(excellent_form) + len(good_form) + len(average_form)
scoring_rate = (scoring_teams / total_goals) * 100

print(f"\n {scoring_rate:.0f}% of teams scored this gameweek")
