import requests
from bs4 import BeautifulSoup
import re
import os
from functions import *

schoolName = "Sebring"
schoolLink = "mckinley-trojans-(sebring,oh)"

url = "https://maxpreps.com/high-schools/" + schoolLink + "/basketball/schedule.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Contains HTML of team names played
schoolsPlayedSoup = soup.select(".contest-type-indicator")
scoresSoup = soup.select(".score")

# Lists containing game information
schoolsPlayed = [] # Contains names of schools played
winLoss = []
scores = [] # Contains temporary strings of 

# Store names of schools played 
for x in schoolsPlayedSoup:
    name = (x.text.split('(', 1)[0]).strip() # School name without whitespace
    schoolsPlayed.append(name)

# Regex patterns
winOrLossRegex = re.compile(r'\(\D\)') # Gets (W) or (L) at start
scoreRegex = re.compile(r'[0-9]{1,3}') # Gets between 1-3 digits

# Fill lists of school names, win/loss, and scores
for x in scoresSoup:
    match = winOrLossRegex.search(x.text).group().strip()
    winOrLoss = match[1:2] # Gets 'W' or 'L'
    match = scoreRegex.findall(x.text) # Holds list of this team's score and opponent's score
    winLoss.append(winOrLoss)
    scores.append(match) 
    print(winOrLoss + " " + match[0] + " - " + match[1])

# Error checking
assert(len(schoolsPlayed) == len(winLoss) == len(scores))

# Holds my custom database numbers and team values (outside of project)
databaseSchoolNumbers = [["Jackson Milton", 1], ["Lowellville", 2], ["McDonald", 3], ["Mineral Ridge", 4], ["Sebring", 5], ["Springfield", 6], ["Waterloo", 7], ["Western Reserve", 8]]

# Create sql file
output = open("output.sql", 'w')
output.write("INSERT INTO game VALUES\n")

thisSchoolNum = findIndexOfSchoolName(schoolName, databaseSchoolNumbers)

"""
TODO: Output date
TODO: Make functions and clean up code
"""

# For every game, output into sql file
for idx, game in enumerate(schoolsPlayed):
    opponentSchoolNum = findIndexOfSchoolName(schoolsPlayed[idx], databaseSchoolNumbers)
    opponentSchoolName = "NULL"
    if(opponentSchoolNum == -1):
        opponentSchoolNum = "NULL"
        opponentSchoolName = "'" + schoolsPlayed[idx] + "'"

    string = f"(NULL, {thisSchoolNum}, {opponentSchoolNum}, {scores[idx][0]}, {scores[idx][1]}, {opponentSchoolName}, NULL, 2019),\n"
    output.write(string)