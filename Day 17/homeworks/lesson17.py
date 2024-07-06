
# N1
# Write a function that takes a list of
# numbers as input and returns the sum of all the numbers in the list.

# დაწერეთ ფუნქცია, რომელიც შეყვანის სახით მიიღებს
# რიცხვების სიას და აბრუნებს სიაში ყველა რიცხვის ჯამს.


 
# def user_numbers(numbers):
#     result = 0
#     for i in numbers:
#         result = result + i
#     return result

# numbers = [24, 23, 25, 67, 12, 33]

# print(user_numbers(numbers))


# N2
# Write a function that takes a list of strings as
# input and returns a new list containing only the strings that have a length greater than 5.

# დაწერეთ ფუნქცია, რომელიც მიიღებს სტრიქონების სიას
# შეყვანად და აბრუნებს ახალ სიას, რომელიც შეიცავს მხოლოდ 5-ზე მეტი სიგრძის სტრიქონებს

# def filter(strings_list):
#     filtered_list = []
#     for word in strings_list:
#         if len(word) > 5:
#             filtered_list.append(word)
    
#     return filtered_list

# car = ["toyuta", "bmw", "ford", "lamborghini", "porshe"]

# print(filter(car))


# N3
# Write a function that takes a list of numbers as input
# and returns a new list containing only the even numbers from the original list

# დაწერეთ ფუნქცია, რომელიც შეყვანის სახით იღებს რიცხვების
# სიას და აბრუნებს ახალ სიას, რომელიც შეიცავს მხოლოდ ლუწი რიცხვებს საწყისი სიიდან

# def even_num(numbers):
#     even_num_list = []

#     for num in numbers:
#         if num % 2 == 0:
#             even_num_list.append(num)

#     return even_num_list

# numbers = [1, 3, 4, 5, 6, 12, 34, 33, 15, 9]

# print(even_num(numbers))


# N4
# Write a function that takes a list of
# numbers as input and returns the largest number in the list.

# დაწერეთ ფუნქცია, რომელიც შეყვანის სახით იღებს
# რიცხვების სიას და აბრუნებს სიაში ყველაზე დიდ რიცხვს.

# def num(numbers):
#     return max(numbers)

# print(num([1, 34, 2, 5, 3, 7, 19, 66, 31]))


# N5
# Write a function that takes a list of strings
# as input and returns a new list containing only the strings that start with the letter 'a'.

# დაწერეთ ფუნქცია, რომელიც მიიღებს სტრიქონების სიას შესაყვანად და აბრუნებს ახალ სიას,
# რომელიც შეიცავს მხოლოდ ასო "a"-ს დაწყებულ სტრიქონებს

# def filter_list(str_list):
#     filtered_list = []
#     for word in str_list:
#         if word[0] == "a":
#             filtered_list.append(word)

#     return filtered_list

# words = ["anmier", "trek", "alaska", "axalcixe", "opel"]

# print(filter_list(words))  


# N6
# Write a function that takes a list of numbers
# as input and returns a new list containing the square of each number.

# დაწერეთ ფუნქცია, რომელიც იღებს რიცხვების სიას შეყვანის
# სახით და აბრუნებს ახალ სიას, რომელიც შეიცავს თითოეული რიცხვის კვადრატს

# def squared_numbers(numbers):
#     squared_numbers_list = []
#     for num in numbers:
#         squared_numbers_list.append(num * num)

#     return squared_numbers_list

# print(squared_numbers([2,4,5,6,4,3,5,24,12]))


# N7
# Write a function that takes a list of strings as input
# and returns a new list containing the lengths of each string.

# დაწერეთ ფუნქცია, რომელიც იღებს სტრიქონების სიას შეყვანის სახით
# და აბრუნებს ახალ სიას, რომელიც შეიცავს თითოეული სტრიქონის სიგრძეს

# def leght_string(text):
#     leght_string_list = []

#     for leght in text:
#         leght_string_list.append(len(leght))

#     return leght_string_list

# print(leght_string(["toyota","terminator","4ranner","naxvamdis"]))


# N8
# Write a function that takes a list of
# numbers as input and returns the sum of all the numbers that are greater than 10. 

# დაწერეთ ფუნქცია, რომელიც შეყვანის სახით იღებს რიცხვების
# ჩამონათვალს და აბრუნებს ყველა რიცხვის ჯამს, რომლებიც 10-ზე მეტია

# def sum_of_numbers(numbers):
#     result = 0

#     for num in numbers:
#         if num > 10:
#             result = result + num

#     return result

# print(sum_of_numbers([1,3,9,12,23,54,77,23,2]))

