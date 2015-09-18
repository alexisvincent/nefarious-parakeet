import sys
sys.path.append('../src/')

from OutputParser import getData;

subcaseID = 2
gridID = 100

dataDictionary = getData('./Data/Output.pch')

print dataDictionary[subcaseID][gridID]
