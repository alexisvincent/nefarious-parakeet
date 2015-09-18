import re

subcases = dict()
currentSubcase = 0
gridBuilder = dict()

numberSearch = re.compile('-?\d+(?:\.\d+(?:E[-+]\d+)?)?')

def parseLine(line):
    global currentSubcase 

    if currentSubcase > 0:
        ## We have read at least one subcase at this point
        if line.startswith('$SUBCASE'):
            handleSubcase(line)
        else:
            handleGridLine(line)
    ## handled like this for optimum speed
    elif line.startswith('$SUBCASE'):
        handleSubcase(line)


def handleSubcase(line):
    global currentSubcase
    subcaseID = int(numberSearch.search(line).group())
    subcases[subcaseID] = dict()
    currentSubcase = subcaseID

def parseNumber(num):
    return float(num.replace('E', 'e').replace('+', ''))

def saveGrid():
    subcases[currentSubcase][int(gridBuilder[2][0])] = (
            parseNumber(gridBuilder[2][1]), 
            parseNumber(gridBuilder[2][2]), 
            parseNumber(gridBuilder[2][3]), 
            parseNumber(gridBuilder[1][0]),
            parseNumber(gridBuilder[1][1]),
            parseNumber(gridBuilder[1][2]),
            parseNumber(gridBuilder[0][0]),
            parseNumber(gridBuilder[0][1]),
        )

def handleGridLine(line):
    gridLine = numberSearch.findall(line.replace('-CONT-', ''))
    gridBuilder[len(gridLine) - 2] = gridLine

    
    if(len(gridLine) == 2):
        saveGrid()

def getData(fileName):
    global subcases
    subcases.clear()
    with open(fileName, "r") as file:
        for line in file:
            parseLine(line)
    file.close()
    return subcases

