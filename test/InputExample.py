import sys
sys.path.append('../src/')

from InputParser import getData;

p1 = (0, 0, 0) # Line point 1
p2 = (0, 1, 1) # Line point 2
r = 10 # Distance of data point from line

dataDictionary = getData('./Data/Input.pch', p1, p2, r)

print dataDictionary
