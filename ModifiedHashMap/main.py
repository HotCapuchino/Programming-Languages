from HashMap import ModifiedDict


modDict = ModifiedDict()
modDict.update({'2': 4})
modDict.update({'3': 9})
modDict['1'] = 2
modDict['(2, 5)'] = 100
modDict.ploc['(>= 3, > 1)']
del modDict['1']
print(modDict.iloc[1])