# N1

# Write a function that accepts a string, and returns the same
# string with all even indexed characters in each word upper cased,
#  and all odd indexed characters in each word lower cased.
#  The indexing just explained is zero based, so the zero-ith index
#  is even, therefore that character should be upper cased
#  and you need to start over for each word.

# def to_weird_case(words):
#     words = words.split(" ")
    
#     res_list = []
    
#     for word in words:
#         modified_str = ""
        
#         for i in range(len(word)):
#             if i %2 == 0:
#                 modified_str += word[i].upper()
#             else:
#                 modified_str += word[i].lower()
        
#         res_list.append(modified_str)
        
#     return " ".join(res_list)

# N2


# Write a method (or function, depending on the language)
# that converts a string to camelCase, that is,
# all words must have their first letter capitalized and spaces must be removed.

# def camel_case(str):
#     res_list = []
    
#     str = str.split(" ")
    
#     for word in str:
#         res_list.append(word.capitalize())
    
#     return "".join(res_list)
        
# N3

# ATM machines allow 4 or 6 digit PIN codes and
# PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

# If the function is passed a valid PIN string, return true, else return false.

# def validate_pin(pin):
#     if len(pin) == 4 or len(pin) == 6:
#         is_valid = True
        
#         numbers = "0123456789"
        
#         for i in pin:
#             if i not in numbers:
#                 is_valid = False
                
#         return is_valid
#     return False