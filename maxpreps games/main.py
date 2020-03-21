import requests
from bs4 import BeautifulSoup
import re
import os
from functions import *


# CUSTOM VARIABLES NEEDING UPDATED BELOW
########################################

schoolName = "Sebring"
databaseSchoolNumbers = [["Jackson Milton", 1], ["Lowellville", 2], ["McDonald", 3], ["Mineral Ridge", 4], ["Sebring", 5], ["Springfield", 6], ["Waterloo", 7], ["Western Reserve", 8]]

########################################



# Finds the index of the current school being worked on
thisSchoolNum = findIndexOfSchoolName(schoolName, databaseSchoolNumbers)

url = "https://maxpreps.com/high-schools/mckinley-trojans-(sebring,oh)/basketball/schedule.htm"
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
dates = fillDatesList(dateSoup, dateRegex, year) # Contains lists for each date, 0 index is for month, 1 index is for day
winLoss = [] # W/L
scores = [] # Contains lists for each game, 0 index is this team, 1 index is opponent
fillWinLossAndScoresList(scoresSoup, winOrLossRegex, scoreRegex, winLoss, scores) # Fill winLoss[] and scores[] lists

# Error checking
assert(len(schoolsPlayed) == len(winLoss) == len(scores) == len(dates))

# Outputs sql file ready for insertion
outputSQL(schoolsPlayed, databaseSchoolNumbers, thisSchoolNum, scores, dates, year)