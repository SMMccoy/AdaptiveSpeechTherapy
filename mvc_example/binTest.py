import json

word_list_read = open(".\demofile4.json","r")
word_list = json.loads(word_list_read.read())
word_list_read.close()
bins = [[] for i in range(10)]

for word in word_list:
    diff = word_list[word]["base_difficulty"]
    diff_ = word_list[word]["scaled_difficulty"]

    bins[round(diff)+diff_-1].append([word,round(diff,2),diff_])


binWidth = 3
currentBin = 5
minBin = currentBin - 1
maxCurrent = currentBin + 1

