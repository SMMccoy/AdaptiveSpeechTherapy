import json

f = open("demofile.json","r")
oldDict = json.loads(f.read())

for x in oldDict:
    length = len(x)
    oldDict[x]["length"] = length
    syn = oldDict[x]["synonyms"]
    syn = syn.split("|")
    oldDict[x]["synonyms"] = syn
    startingLetter = x[0]
    oldDict[x]["startingLetter"] = startingLetter

a = open("demofile1.json", "w")
a.write(json.dumps(oldDict,indent=4))
