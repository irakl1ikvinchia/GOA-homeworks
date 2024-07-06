# N1

# Given a set of numbers, return the additive inverse of each. 
# Each positive becomes negatives, and the negatives become positives.

def invert(lst):
    return [-num for num in lst]

#___________________________________________________________________________________________

# N2

# Write a function that takes an array of words and smashes 
# them together into a sentence and returns the sentence. 
# You can ignore any need to sanitize words or add punctuation, 
# but you should add spaces between each word. Be careful, 
# there shouldn't be a space at the beginning or the end of the sentence!

def smash(words):
    result = " ".join(words)
    return result


#___________________________________________________________________________________________

# N3

# Complete the function that takes two integers 
# (a, b, where a < b) and return an array of all 
# integers between the input parameters, including them.

def between(a,b):
    result = []
    for i in range(a, b + 1):
        result.append(i)
        
    return result

#___________________________________________________________________________________________

# N4