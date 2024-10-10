# N1

# Write a function that takes an array of numbers
# and returns the sum of the numbers. 
# The numbers can be negative or non-integer. 
# If the array does not contain any numbers then you should return 0.

# def sum_array(a):
#     sum = 0
    
#     for num in a:
#         sum = sum + num
        
#     return sum


#______________________________________________________________________________________________


# N2

# Write a function which calculates 
# the average of the numbers in a given list.
# Note: Empty arrays should return 0.

# def find_average(numbers):
#     if not numbers:
#         return 0
#     return sum(numbers) / len(numbers)


#_______________________________________________________________________________________________


# N3

# Given an array of integers.
# Return an array, where the first 
# element is the count of positives 
# numbers and the second element is 
# sum of negative numbers. 0 is neither positive nor negative.
# If the input is an empty array or is null, return an empty array

# def count_positives_sum_negatives(arr):
#     if len(arr) == 0:
#         return arr
#     count = 0
#     sum = 0
#     for i in arr:
#         if i > 0:
#             count += 1
#         else:
#             sum += i
#     return [count , sum]

#___________________________________________________________________________________________________


# N4

# Your task is to make a function that can take any 
# non-negative integer as an argument and return it 
# with its digits in descending order. Essentially, 
# rearrange the digits to create the highest possible number.

# def descending_order(num):
#     num = str(num)
#     num = list(num)
    
#     new_arr = []    
#     for i in num:
#         new_arr.append(int(i))
#     new_arr.sort(reverse = True)
    
    
#     res_str = ""
#     for x in new_arr:
#         res_str += str(x)
#     return int(res_str)

#_____________________________________________________________________________________________________

# N5

# Create a function that returns the sum of 
# the two lowest positive numbers given an 
# array of minimum 4 positive integers. 
# No floats or non-positive integers will be passed.
# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# def sum_two_smallest_numbers(numbers):
#     numbers.sort()
#     return numbers[0] + numbers[1]

#______________________________________________________________________________________________________

# N6

# Complete the method/function so that it 
# converts dash/underscore delimited words 
# into camel casing. The first word within 
# the output should be capitalized only 
# if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

# def to_camel_case(text):
#     words = text.replace("_","-").split("-")
#     result = words[0]
#     words = words[1:]
#     for i in words:
#         result += i.capitalize()
        
#     return result

#_____________________________________________________________________________________________________

# N7

# Complete the method/function so that it converts 
# dash/underscore delimited words into camel casing. 
# The first word within the output should be 
# capitalized only if the original word was capitalized 
# (known as Upper Camel Case, also often referred to as Pascal case). 
# The next words should be always capitalized.

# def to_camel_case(text):
#     words = text.replace("_","-").split("-")
#     result = words[0]
#     words = words[1:]
#     for i in words:
#         result += i.capitalize()
        
#     return result