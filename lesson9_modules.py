import string_utils
import random

print(string_utils.is_vowels('a'))
print(string_utils.count_vowels('hello world'))

def roll_dice():
    return random.randint(1, 6)

print("Number on a rolled Dice: ",roll_dice())