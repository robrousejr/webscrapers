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