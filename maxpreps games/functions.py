import re

# Finds location of school name in a list containing school names and their database numbers
# Returns -1 if school name is not found 
def findIndexOfSchoolName(school, schoolsList):
    index = 1 # Counter

    # Check if in list
    if(any(school in i for i in schoolsList)):
        for list in schoolsList:
            if(list[0] == school):
                return index
            index = index + 1
    else:
        return -1

# Make any 1 digit number a 2 digit number
def makeTwoDigits(num):
    numDigits = len(str(num))
    if(numDigits == 1):
        newNum = "0" + str(num)
        return newNum
    else:
        return num

# Returns correct year of certain game
def getYearOfGame(month, seasonYear):
    if(month > 6):
        return str(seasonYear)
    else:
        return str(seasonYear + 1)

# Extracts 4 digit year out of soup
def extractYear(yearRegex, soup):
    return re.search(yearRegex, soup).group().strip()

# Fill schoolsPlayed list of school names
def fillSchoolsPlayedList(schoolsPlayedSoup):
    tmpList = []
    for x in schoolsPlayedSoup:
        name = (x.text.split('(', 1)[0]).strip() # School name without whitespace
        tmpList.append(name)
    return tmpList