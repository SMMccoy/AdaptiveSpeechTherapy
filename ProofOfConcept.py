import pyttsx3
engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)


voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

dict = ['dog', 'cat', 'house']

for word in dict:
    engine.say(word)
    engine.runAndWait()

    answer = input()
    if answer == word:
        print("CORRECT")
    else:
        print("WRONG")

engine.stop()


