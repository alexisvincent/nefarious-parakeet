dictionary = dict()
point1 = 0
point2 = 0

def lineFilter(item):
    return True

def addGridItem(item):
    if lineFilter(item):
        dictionary[item[0]] = (item[1], item[2], item[3]) 

def parseNumber(num): 
    if '-' in num[1:]:
        return float(num[0] + num[1:].replace('-', 'e-'))
    return float(num)

def parseLine(line):
    if (line.startswith('GRID')):
        addGridItem((
            int(line[8:16]), 
            parseNumber(line[24:32]), 
            parseNumber(line[32:40]), 
            parseNumber(line[40:48])
        ))

def getData(fileName, p1, p2):

    point1 = p1
    point2 = p2

    with open(fileName, "r") as file:
        for line in file:
            parseLine(line)
    file.close()
    return dictionary


