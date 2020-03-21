import requests
from bs4 import BeautifulSoup
import re

schoolName = "mckinley-trojans-(sebring,oh)"
url = "https://maxpreps.com/high-schools/" + schoolName + "/basketball/schedule.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Contains HTML of team names played
schoolsPlayedSoup = soup.select(".contest-type-indicator")
scoresSoup = soup.select(".score")

schoolsPlayed = [] # Contains names of schools played
winLoss = []
tmpScores = [] # Contains temporary strings of 

# Store names of schools played 
for x in schoolsPlayedSoup:
    name = (x.text.split('(', 1)[0]).strip() # School name without whitespace
    schoolsPlayed.append(name)

# Regex patterns
winOrLossRegex = re.compile(r'\(\D\)') # Gets (W) or (L) at start
scoreRegex = re.compile(r'[0-9]{1,3}') # Gets between 1-3 digits

for x in scoresSoup:
    match = winOrLossRegex.search(x.text).group().strip()
    winOrLoss = match[1:2] # Gets 'W' or 'L'
    match = scoreRegex.findall(x.text) # Holds list of this team's score and opponent's score
    winLoss.append(winOrLoss)
    tmpScores.append(match) 
    print(winOrLoss + " " + match[0] + " - " + match[1])