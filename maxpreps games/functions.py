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

# Fill dates list
def fillDatesList(dateSoup, dateRegex, year):
    dates = []
    for x in dateSoup:
        match = dateRegex.findall(x.text) # Holds list of month, day
        match[0] = makeTwoDigits(match[0]) # Month
        match[1] = makeTwoDigits(match[1]) # Day
        tmpYear = getYearOfGame(int(match[0]), int(year))
        dates.append(tmpYear + "-" + match[0] + "-" + match[1]) # Format: yyyy-mm-dd
    return dates

# Fills the winLoss[] list and the scores[] list
def fillWinLossAndScoresList(scoresSoup, winOrLossRegex, scoreRegex, winLoss, scores, errList):
    for iterNum, x in enumerate(scoresSoup):
        match = winOrLossRegex.search(x.text)

        # Match found
        if(match != None):
            match = match.group().split()
            winOrLoss = match[0][1:2] # Gets 'W' or 'L'
            match = scoreRegex.findall(x.text) # Holds list of this team's score and opponent's score
            # If loss, swap order of scores match list
            if(winOrLoss == "L"):
                tmp = match[0]
                match[0] = match[1]
                match[1] = tmp
            # print(winOrLoss + " " + match[0] + " - " + match[1])
            winLoss.append(winOrLoss)
            scores.append(match)
        else:
            # Keeps track of error indexes to be removed from other lists
            errList.append(iterNum)

# Deletes error indexes in schoolsPlayed, dates lists
def deleteErrIndexes(errList, schoolsPlayed, dates):
    for index in errList:
        del schoolsPlayed[index]
        del dates[index]

# Outputs games into a SQL file
def outputSQL(schoolsPlayed, databaseSchoolNumbers, thisSchoolNum, scores, dates, year):
    # Create sql file
    output = open("output.sql", 'w')
    output.write("INSERT INTO game VALUES\n")

    for iterNum, game in enumerate(schoolsPlayed):
        opponentSchoolNum = findIndexOfSchoolName(schoolsPlayed[iterNum], databaseSchoolNumbers)
        opponentSchoolName = "NULL"
        if(opponentSchoolNum == -1):
            opponentSchoolNum = "NULL"
            opponentSchoolName = "'" + schoolsPlayed[iterNum] + "'"

        string = f"(NULL, {thisSchoolNum}, {opponentSchoolNum}, {scores[iterNum][0]}, {scores[iterNum][1]}, {opponentSchoolName}, '{dates[iterNum]}', {int(year)}),\n"
        output.write(string)