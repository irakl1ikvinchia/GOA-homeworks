# N1
# Given an array of integers your solution should find the smallest integer

# def find_smallest_int(arr):
#     smallest_int =  arr[0]
    
#     for num in arr:
#         if smallest_int > num:
#             smallest_int = num 
            
#     return smallest_int

# N2
# Write a function that removes the spaces from the string, then return the resultant string

# def no_space(x):
#     result = ""
    
#     for char in x:
#         if char != " ":
#             result = result + char
            
#     return result

# N3

# Implement a function which convert the given boolean value into its string representation

# def boolean_to_string(b):
#     return str(b)

# N4
# Write a function that takes an array of numbers and returns the sum of the numbers.
# The numbers can be negative or non-integer.
# If the array does not contain any numbers then you should return 0

# def sum_array(a):
#     sum = 0
    
#     for num in a:
#         sum = sum + num
        
#     return sum

# N5
# Write a function to convert a name into initials.
# This kata strictly takes two words with one space in between them

# def abbrev_name(name):
#     name = name.upper()
#     splited_name = name.split(" ")
    
#     firstname = splited_name[0]
#     lastname = splited_name[1]
    
#     result = firstname[0] + "." + lastname[0]
    
#     return result

# N6
# Given an array of integers, return a new array with each value doubled

# def maps(list):
#     doubled_numbers = []
    
#     for num in list:
#         doubled_numbers.append(num * 2)
        
#     return doubled_numbers

# N7
# Write a function which converts the input string to uppercase

# def make_upper_case(s):
#     s = s.upper()
#     return s

# N8
# Write a function which calculates the average of the numbers in a given list


# def find_average(numbers):
#     if not numbers:
#         return 0
#     return sum(numbers) / len(numbers)


# N9
# Write function bmi that calculates body mass index (bmi = weight / height2).


# def bmi(weight, height):
#     bmii = weight / height ** 2
    
#     if bmii <= 18.5:
#         return "Underweight"

#     if bmii <= 25.0: 
#         return "Normal"

#     if bmii <= 30.0:
#         return "Overweight"

#     if bmii > 30:
#         return "Obese"