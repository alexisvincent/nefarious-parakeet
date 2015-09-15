import sys
sys.path.append('../src/')

from InputParser import getData;

dataDictionary = getData('./Data/Input.pch', 0, 0)
print dataDictionary

