# This program checks if a given phrase is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backward as forward. 
# The program removes non-alphanumeric characters and ignores case before performing the check.

import re

def is_palindrome(phrase):
    phrase = re.sub(r'[^a-zA-Z0-9]', '', phrase.lower())

    print("Cette phrase est bien un palindrome !" if phrase == phrase[::-1] else "Cette phrase n'est pas un palindrome")

txt = input("Entrer un mot ou une phrase : ")
is_palindrome(txt)
