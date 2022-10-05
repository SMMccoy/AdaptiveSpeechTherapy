import requests
import json

wordDict = {}
wordList = []
for line in open("./Aph/wordList"):
    wordList = line.split(";")

for x in wordList:
    params = {'sysparm_display_value': True, 'sysparm_exclude_reference_link': 'true'}
    
    myURL = "http://thesaurus.altervista.org/thesaurus/v1?word={}&language=en_US&key=HNwd3gberxYk07G3JAaK&output=json".format(x)
    response = requests.get(url = myURL,params=params)
    
    if response.status_code == 404:
        print(x)
    else:
        i = 0
        catcher = True
        category = " "
        synonyms = " "
        while catcher:
            try:
                category = category +";"+response.json()['response'][i]['list']["category"]
                synonyms = synonyms + ";"+response.json()['response'][i]['list']['synonyms']
                wordDict[x] = {}
                i += 1
            except:
                catcher = False
        wordDict[x]["category"] = category
        wordDict[x]["synonyms"] = synonyms
        
f = open("demofile.json", "w")
f.write(json.dumps(wordDict,indent=4))
