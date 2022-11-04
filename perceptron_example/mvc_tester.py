import random
import pyttsx3
import pyceptron.Module
from pyceptron import Module
from pyceptron.Module import calculate_difficulty

engine = pyttsx3.init(None, True)
engine.setProperty("rate", 125)
difficultyArrays = {}
correct_answers = []


f = open("list.txt")
text = f.read()
textArray = text.split("\n")
#print(text)
vowels = ["a", "e", "i", "o", "u"]
random.shuffle(textArray)

for w in textArray:
    if difficultyArrays.get(calculate_difficulty(w)) is None:
        difficultyArrays[calculate_difficulty(w)] = []
    difficultyArrays[calculate_difficulty(w)].append(w)

f.close()

machine = pyceptron.Module.Perceptron(26 * 22, 2, 0)

def get_amount_of_predicted_wrong_words():
    amount = 0
    for w in textArray:
        if not machine.input(w):
            amount += 1
    return amount

def get_predicted_wrong_words():
    words = []
    for w in textArray:
        if not machine.input(w):
            words.append(w)
    return words

def get_predicted_correct_words():
    words = []
    for w in textArray:
        if machine.input(w):
            words.append(w)
    return words

give_incorrect = True
counter = 0
while True:
    print(get_amount_of_predicted_wrong_words())
    words = get_predicted_wrong_words()
    correct_words = get_predicted_correct_words()

    level = 0
    for w in correct_words:
        w_level = calculate_difficulty(w)
        if w_level > level:
            level = w_level

    incorrect_level = 1000
    for w in words:
        wl_level = calculate_difficulty(w)
        if wl_level < incorrect_level:
            incorrect_level = wl_level

    level = max(level, incorrect_level)
    print("Level: ", level, " | incorrect level: ", incorrect_level)
    random.shuffle(words)
    random.shuffle(correct_words)
    currentWord = "oooooooooooooooooooooooooooooooooooooooooooooo"

    if len(words) > 0:
        for incWord in words:
            if level >= calculate_difficulty(incWord) and incWord not in correct_answers:
                if calculate_difficulty(incWord) < calculate_difficulty(currentWord):
                    currentWord = incWord

    if currentWord == "oooooooooooooooooooooooooooooooooooooooooooooo":
        if len(words) > 0:
            for incWord in words:
                if level >= calculate_difficulty(incWord):
                    if calculate_difficulty(incWord) < calculate_difficulty(currentWord):
                        currentWord = incWord

    currentWordCorrect = ""
    if len(correct_words) > 0:
        for corWord in correct_words:
            if level >= calculate_difficulty(corWord) and corWord not in correct_answers:
                if calculate_difficulty(corWord) > calculate_difficulty(currentWordCorrect):
                    currentWordCorrect = corWord

    if currentWordCorrect == "":
        if len(correct_words) > 0:
            for corWord in correct_words:
                if level >= calculate_difficulty(corWord):
                    if calculate_difficulty(corWord) > calculate_difficulty(currentWordCorrect):
                        currentWordCorrect = corWord

    type = ""
    if counter == 2 and currentWordCorrect is not None:
        currentWord = currentWordCorrect
        give_incorrect = True
        type = "Correct"
        counter = 0
    else:
        give_incorrect = False
        type = "Incorrect"
        counter += 1

    print("Word level: ", calculate_difficulty(currentWord))
    print(type + " word = " + currentWord)

    print("spell word or repeat word? (word/r)")
    response = "r"
    while response == "r":
        engine.say(currentWord)
        engine.runAndWait()
        response = input()

    if str.lower(response) == str.lower(currentWord):
        print("Correct!")
        machine.learn(currentWord, True)
        correct_answers.append(currentWord)
    else:
        print("Incorrect!")
        machine.learn(currentWord, False)
        counter = 2
    print(get_predicted_correct_words())
    print()


