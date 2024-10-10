# N1

# Write a function that takes a string of braces, 
# and determines if the order of the braces is valid. 
# It should return true if the string is valid, and false if it's invalid.

# This Kata is similar to the Valid Parentheses Kata, 
# but introduces new characters: brackets [], and curly braces {}. 
# Thanks to @arnedag for the idea!

# All input strings will be nonempty, and will only consist of 
# parentheses, brackets and curly braces: ()[]{}.

# What is considered Valid?
# A string of braces is considered valid if all braces are 
# matched with the correct brace.


def valid_braces(s):
    while "()" in s or "[]" in s or "{}" in s:
        s = s.replace("()", "")
        s = s.replace("{}", "")
        s = s.replace("[]", "")
        
    return s == ""


#_______________________________________________________________________________________________________


# N2

# Welcome.

# In this kata you are required to, given a string, 
# replace every letter with its position in the alphabet.

# If anything in the text isn't a letter, ignore it and don't return it.

# "a" = 1, "b" = 2, etc.


def alphabet_position(text):
    result = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for char in text.lower():
        if char.isalpha():   
            index = alphabet.index(char) + 1
            result.append(str(index))
    
    return " ".join(result)
# ______________________________________________________________________________________________________


# N3

# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace the 
# missing second character of the final pair with an underscore ('_').

def solution(s):
    if len(s) % 2 != 0:
        s += "_"
        
    res = ""
    count = 0
    for char in s:
        res += char
        count += 1
        if count % 2 == 0:
            res += "|"
    return (res.split("|"))[:-1]

# ______________________________________________________________________________________________________

# N4

