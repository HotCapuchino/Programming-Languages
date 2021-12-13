from HashMap import ModifiedDict


modDict = ModifiedDict()
modDict.update({'2': 4})
modDict.update({'3': 9})
modDict['1'] = 2
del modDict['1']
print(modDict.iloc[1])