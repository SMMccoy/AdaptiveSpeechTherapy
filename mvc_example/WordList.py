import json

word_list_read = open("mvc\demofile4.json","r")
word_list = json.loads(word_list_read.read())
