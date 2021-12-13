from HashMap import ModifiedDict


modDict = ModifiedDict()
modDict.update({'2': 4})
modDict.update({'3': 9})
modDict['1'] = 2
print(modDict.iloc[1])