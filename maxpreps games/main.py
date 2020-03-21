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

# Regex patterns
winOrLossRegex = re.compile(r'\(\D\)') # Gets (W) or (L) at start
scoreRegex = re.compile(r'[0-9]{1,3}') # Gets between 1-3 digits
yearRegex = re.compile(r'\d{4}') # Gets first 4 digit number (year)
dateRegex = re.compile(r'[0-9]{1,2}') # Gets date numbers (0 = month, 1 = day)

# Soup objects
schoolsPlayedSoup = soup.select(".contest-type-indicator") # Contains of team names played
scoresSoup = soup.select(".score") # Contains html of scores
dateSoup = soup.select(".event-date") # Contains html of dates

# 4 digit year of starting point in season (ex: 2019 for 2019-20 season)
year = extractYear(yearRegex, (soup.select("#ctl00_NavigationWithContentOverRelated_ContentOverRelated_PageHeaderUserControl_Team"))[0].text)

# Lists containing game information
schoolsPlayed = fillSchoolsPlayedList(schoolsPlayedSoup) # Contains names of schools played
winLoss = [] # W/L
scores = [] # Contains lists for each game, 0 index is this team, 1 index is opponent
dates = [] # Contains lists for each date, 0 index is for month, 1 index is for day

# Fill winLoss, scores lists
for x in scoresSoup:
    match = winOrLossRegex.search(x.text).group().strip()
    winOrLoss = match[1:2] # Gets 'W' or 'L'
    match = scoreRegex.findall(x.text) # Holds list of this team's score and opponent's score
    winLoss.append(winOrLoss)
    scores.append(match)
    print(winOrLoss + " " + match[0] + " - " + match[1])

# Fill dates list
for x in dateSoup:
    match = dateRegex.findall(x.text) # Holds list of month, day
    match[0] = makeTwoDigits(match[0]) # Month
    match[1] = makeTwoDigits(match[1]) # Day
    tmpYear = getYearOfGame(int(match[0]), int(year))
    dates.append(tmpYear + "-" + match[0] + "-" + match[1]) # Format: yyyy-mm-dd

# Error checking
assert(len(schoolsPlayed) == len(winLoss) == len(scores) == len(dates))

# Holds my custom database numbers and team values (outside of project)
databaseSchoolNumbers = [["Jackson Milton", 1], ["Lowellville", 2], ["McDonald", 3], ["Mineral Ridge", 4], ["Sebring", 5], ["Springfield", 6], ["Waterloo", 7], ["Western Reserve", 8]]

# Create sql file
output = open("output.sql", 'w')
output.write("INSERT INTO game VALUES\n")

thisSchoolNum = findIndexOfSchoolName(schoolName, databaseSchoolNumbers)

"""
TODO: Output date ("yyyy-mm-dd")
TODO: Make functions and clean up code
"""

# For every game, output into sql file
for iterNum, game in enumerate(schoolsPlayed):
    opponentSchoolNum = findIndexOfSchoolName(schoolsPlayed[iterNum], databaseSchoolNumbers)
    opponentSchoolName = "NULL"
    if(opponentSchoolNum == -1):
        opponentSchoolNum = "NULL"
        opponentSchoolName = "'" + schoolsPlayed[iterNum] + "'"

    string = f"(NULL, {thisSchoolNum}, {opponentSchoolNum}, {scores[iterNum][0]}, {scores[iterNum][1]}, {opponentSchoolName}, '{dates[iterNum]}', {int(year)}),\n"
    output.write(string)