import sys
sys.path.append('../src/')

from InputParser import getData, lineReducer;

p1 = (0, 0, 0) # Line point 1
p2 = (0, 1, 1) # Line point 2
r = 5 # Distance of data point from line

dataDictionary = getData('./Data/Input.pch')

print lineReducer(dataDictionary, p1, p2, r)
