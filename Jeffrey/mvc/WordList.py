import json

word_list_read = open("demofile4.json","r")
word_list = json.loads(word_list_read.read())

# word_list = [
#     "Hello",
#     "Testing",
#     "One",
#     "Two",
#     "Three"
# ]