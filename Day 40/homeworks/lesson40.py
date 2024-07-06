# N1

# Write a function named first_non_repeating_letter† 
# that takes a string input, and returns the first 
# character that is not repeated anywhere in the string.

# For example, if given the input 'stress', 
# the function should return 't', since the 
# letter t only occurs once in the string, 
# and occurs first in the string.

# As an added challenge, upper- and lowercase 
# letters are considered the same character, 
# but the function should return the correct 
# case for the initial letter. For example, the input 'sTreSS' should return 'T'.

# If a string contains all repeating characters, 
# it should return an empty string ("");

# † Note: the function is called 
# firstNonRepeatingLetter for historical 
# reasons, but your function should handle any Unicode character.


# def first_non_repeating_letter(s):
#     s_lower = s.lower()
#     for i in s:
#         if s.lower().count(i.lower()) == 1:
#             return i
       
#     return ""
    

#______________________________________________________________________________________________________


# N2

# The goal of this exercise is to convert 
# a string to a new string where each character 
# in the new string is "(" if that character 
# appears only once in the original string, or ")" 
# if that character appears more than once in the 
# original string. Ignore capitalization when 
# determining if a character is a duplicate.

# def duplicate_encode(word):
#     word_lower = word.lower()
#     result = ""
    
#     for i in word_lower:
#         if word_lower.count(i) == 1:
#             result += "("
#         else:
#             result += ")"
#     return result

#______________________________________________________________________________________________________