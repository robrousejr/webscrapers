import requests
from bs4 import BeautifulSoup
import re

schoolName = "mckinley-trojans-(sebring,oh)"
url = "https://maxpreps.com/high-schools/" + schoolName + "/basketball/schedule.htm"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Contains HTML of team names played
schoolsPlayedSoup = soup.select(".contest-type-indicator")

# Contains names of schools played
schoolsPlayed = []

for x in schoolsPlayedSoup:
    name = (x.text.split('(', 1)[0]).strip() # School name without whitespace
    schoolsPlayed.append(name)