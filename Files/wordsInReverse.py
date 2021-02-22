import pickle
exampleDict = {1: 'Hello', 2: 'World', 3: 'From', 4: 'Python'}
with open("/Ghosty's Files/Programming/Python/Files/pickledDict.pckl","wb") as pickleObject:
    pickle.dump(exampleDict, pickleObject)
with open("/Ghosty's Files/Programming/Python/Files/pickledDict.pckl","rb") as pickleObject:
    unPickledDict = pickle.load(pickleObject)
print(unPickledDict==exampleDict)