import random
from termcolor import colored

def get_user_input(missing_word):
    is_not_alpha_loop = True
    while is_not_alpha_loop:
        if missing_word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            user_word = input("Enter an {}: ".format(missing_word.lower()))
        else:
            user_word = input("Enter a {}: ".format(missing_word.lower()))

        # handles improper user input
        if user_word.isalpha() == False:
            print("Numbers and symbols are not supported. Please enter only letters.")
        else:
            is_not_alpha_loop = False

    # appends user input to appropriate missing_word key in user_input
    if missing_word not in user_input:
        user_input[missing_word] = list()
    user_input[missing_word].append(random_color(user_word))

# picks random word from user_input
def get_random_word(part_of_speech):
    word = user_input[part_of_speech][random.randint(0, len(user_input[part_of_speech]) - 1)]
    user_input[part_of_speech].remove(word)
    return word

def random_color(word):
    colors = ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    random_color_index = random.randint(0, len(colors)-1)
    word = colored(word, colors[random_color_index])
    return word

def create_story(story):
    story_list = story.split(" ")

    for item in story_list:
        if item[0] == "_": # checks if word is a missing_word
            if item[len(item) - 1] == "_":
                last_char = len(item) - 1
            else:
                last_char = len(item) - 2
            missing_words[item[1:last_char]] = ""
            missing_word = item[2:last_char] # removes missing_word identifiers

            # checks if missing_word is a key in word_count, updates count if it is
            if missing_word not in word_count:
                word_count[missing_word] = 1
                get_user_input(missing_word)
            elif word_count[missing_word] < int(item[1]):
                word_count[missing_word] += 1
                get_user_input(missing_word)

    # chooses a random word for story
    for item in missing_words:
        missing_words[item] = get_random_word(item[1:])

    # populates user's words back to story
    for index in range(len(story_list)):
        word = story_list[index]
        if word[0] == "_":
            last_char = word[len(word)-1]
            if last_char != "_":
                word = word[1:len(word)-2]
                story_list[index] = missing_words[word] + last_char
            else:
                word = word[1:len(word)-1]
                story_list[index] = missing_words[word]

    finished_story = " ".join(story_list)
    print()
    return finished_story

user_input = {} # {"PART OF SPEECH": "LIST -- USER WORDS"}
word_count = {} # {"PART OF SPEECH": "INT -- COUNT"}
missing_words = {} # {"PART OF SPEECH": "STRING -- RANDOM USER WORD"}

story1 = "_1NAME_ likes to _1VERB_ ice cream. She prefers _1ADJECTIVE_ over _2ADJECTIVE_. _1NAME_ went to the store today to buy some _1ADJECTIVE_ ice cream, but they only had _2ADJECTIVE_ ice cream."

story2 = "_1NOUN_. _2NOUN_. _3NOUN_. _4NOUN_. Long ago, four nations lived together in _5NOUN_. Then, everything changed when the _1ADJECTIVE_ _2NOUN_ Nation attacked. Only the _6NOUN_, master of all four elements, could _1VERB_ them, but when the world needed him most, he _2VERB_. A hundred years passed and my _7NOUN_ and I _3VERB_ the new _6NOUN_, a _2NOUN_ bender named _1NAME_. And although his _2NOUN_ bending skills are _2ADJECTIVE_, he has a lot to _4VERB_ before he's ready to _5VERB_ anyone. But I believe _1NAME_ can _5VERB_ the _8NOUN_."

# print(create_story(story1)) # TEST 
print(create_story(story2))

# -------------- WEBSITE --------------
# def get_missing_words():
#     story_list = story.split(" ")
#
#     for item in story_list:
#         if item[0] == "_" and item[len(item) - 1] == "_": # checks if word is a missing_word
#             missing_words[item] = ""
#             missing_word = item[2:len(item) - 1] # removes missing_word identifiers
#             if missing_word not in user_input:
#                 user_input[missing_word] = list()
#             user_input[missing_word].append("")
#     return user_input
