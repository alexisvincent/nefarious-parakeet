import sys
sys.path.append('../src/')

from OutputParser import getData;

subcaseID = 1
gridID = 100

subcases = getData('./Data/Output.pch')

print subcases[subcaseID][gridID]
