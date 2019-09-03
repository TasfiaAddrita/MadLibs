import random

user_input = {}
word_count = {}
missing_words = {}

story = "_1NAME_ likes to _1VERB_ ice cream. She prefers _1ADJECTIVE_ over _2ADJECTIVE_. _1NAME_ went to the store today to buy some _1ADJECTIVE_ ice cream, but they only had _2ADJECTIVE_ ice cream."

def get_user_input(missing_word):
    if missing_word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
        user_word = input("Enter an {}: ".format(missing_word.lower()))
    else:
        user_word = input("Enter a {}: ".format(missing_word.lower()))
    if missing_word not in user_input:
        user_input[missing_word] = list()
    user_input[missing_word].append(user_word)

def get_random_word(part_of_speech):
    word = user_input[part_of_speech][random.randint(0, len(user_input[part_of_speech]) - 1)]
    user_input[part_of_speech].remove(word)
    return word

def create_story():
    story_list = story.split(" ")

    for item in story_list:
        if item[0] == "_" and item[len(item) - 1] == "_": # checks if word is a missing_word
            missing_words[item] = ""
            missing_word = item[2:len(item) - 1] # removes missing_word identifiers

            if missing_word not in word_count:
                word_count[missing_word] = 1
                get_user_input(missing_word)
            elif word_count[missing_word] < int(item[1]):
                word_count[missing_word] += 1
                get_user_input(missing_word)

    for item in missing_words:
        missing_words[item] = get_random_word(item[2:len(item) - 1])

    for index in range(len(story_list)):
        word = story_list[index]
        if "." in word:
            word = word[:len(word)-1]
        if word in missing_words:
            if "." in story_list[index]:
                story_list[index] = missing_words[word] + "."
            else:
                story_list[index] = missing_words[word]

    finished_story = " ".join(story_list)
    return finished_story

print(create_story())
