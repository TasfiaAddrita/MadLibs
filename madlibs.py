# import random

story_input = ["noun", "verb", "noun", "adjective"]

user_input = {}

for part_of_speech in story_input:
    user_word = input("Enter a {}: ".format(part_of_speech)).lower()
    if part_of_speech not in user_input:
        user_input[part_of_speech] = list()
    user_input[part_of_speech].append(user_word)

# story = "My name is {}. I am {} to get {} ice cream.".format()
# print(user_input)
