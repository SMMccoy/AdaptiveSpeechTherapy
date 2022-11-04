textFile = open("list.txt")
WORD_LIST = textFile.read().split("\n")
textFile.close()

VOWELS = ["a", "e", "i", "o", "u"]
HARD_LETTERS = ["x", "y", "q", "z"]
LENGTH_DIFFICULTY = 1.5
VOWEL_DIFFICULTY = .25
HARD_LETTER_DIFFICULTY = .5

banned_word_list = {}


def calculate_word_difficulty(word):
    v_list = 0
    h_list = 0
    world_length = len(word) * LENGTH_DIFFICULTY
    for letter in word:
        if letter in VOWELS:
            v_list += VOWEL_DIFFICULTY
        if letter in HARD_LETTERS:
            h_list += HARD_LETTER_DIFFICULTY

    return world_length + h_list + v_list


def ban_word(word, length):
    if banned_word_list.get(word):
        banned_word_list[word] = max(length, banned_word_list[word])
    else:
        banned_word_list[word] = length


def get_words_in_level_range(level, range):
    in_range_list = []
    for word in WORD_LIST:
        difficulty = calculate_word_difficulty(word)
        if (level - range) < (difficulty) < (level + range) and banned_word_list.get(word) is None:
            in_range_list.append(word)
    reduce_bans()
    return in_range_list


def reduce_bans():
    to_unban = []
    for key in banned_word_list.keys():
        banned_word_list[key] = banned_word_list.get(key) - 1
        if banned_word_list.get(key) <= 0:
            to_unban.append(key)
    for key in to_unban:
        banned_word_list.pop(key)
        print("Pop")


