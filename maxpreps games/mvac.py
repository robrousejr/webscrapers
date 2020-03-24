import requests
from bs4 import BeautifulSoup
import re
import os

"""
TODO: Scrape mvacbasketball.com to get proper season SQL information
TODO: Make SQL file for season insertion (NULL, Team_id, season year, wins, losses, wlratio)
"""

# CUSTOM VARIABLES NEEDING UPDATED BELOW
########################################

url = "https://mvacbasketball.com/team.php?id=5"
databaseSchoolNumbers = [["Jackson-Milton", 1], ["Lowellville", 2], ["McDonald", 3], ["Mineral Ridge", 4], ["Sebring", 5], ["Springfield", 6], ["Waterloo", 7], ["Western Reserve", 8]]

########################################

# Prepare page soup
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
winLoss = soup.select(".game-score")

# Regex
scoreRegex = re.compile(r'[0-9]{1,3}') # Gets between 1-3 digits
seasonRegex = re.compile(r'season=\d{4}') # Extracts season year
idRegex = re.compile(r'id=\d') # Extracts team ID

# Gets season from URL
season = 2019 # Default season
match = seasonRegex.search(url)
if(match != None):
    match = match.group().split()
    season = match[0][-4:] # Get last 4 characters

# Gets team ID from URL
match = idRegex.search(url)
id = match[0][-1:]

# Counts wins/losses
wins = losses = 0
for x in winLoss:
    match = scoreRegex.findall(x.text) # Holds list of this team's score and opponent's score
    # Win
    if(match[0] > match[1]):
        wins = wins + 1
    else:
        losses = losses + 1

# Create sql file
output = open("output.sql", 'w')
output.write("INSERT INTO season VALUES\n")
output.write(f"(NULL, {int(id)}, {int(season)}, {wins}, {losses}, {round(wins/(wins + losses), 5)});")

