import requests

url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

def get_word_def(word):
    response = requests.get(url + word.lower())
    json_response = response.json()
    return json_response[0]["meanings"][0]['definitions'][0]["definition"]
