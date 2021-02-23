import pickle as pck
exampleDict = {1: 'Hello', 2: 'World', 3: 'From', 4: 'Python'}
with open("pickledDict.pckl","wb") as pickleFile:
    pck.dump(exampleDict,pickleFile)
with open("pickledDict.pckl","rb") as pickleFile:
    loadedDict = pck.load(pickleFile)
    print(loadedDict==exampleDict)
