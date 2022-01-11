from HashMap import ModifiedDict


modDict = ModifiedDict()
modDict.update({'2': 4})
modDict['1.0'] = 22
modDict['1.0'] = 30
modDict['4'] = 5
modDict['3'] = 4
modDict['(2, 5)'] = 100
print(modDict.ploc['(>= 2, >1)'])
