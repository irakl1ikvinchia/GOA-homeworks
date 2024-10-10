# N1
# Write a program that takes asks user for number (use input). 
# If number is even, print that number is even. Else print that number is not even, 
# also print next even number, for example if input is 15, print 16.

# დაწერეთ პროგრამა, რომელიც სთხოვს მომხმარებელს ნომერს (გამოიყენეთ input()). 
# თუ რიცხვი ლუწია, დაბეჭდეთ ეს რიცხვი ლუწია. წინააღმდეგ შემთხვევაში
# დაბეჭდეთ ეს რიცხვი არ არის ლუწი, ასევე დაბეჭდეთ შემდეგი ლუწი რიცხვი, 
# მაგალითად, თუ შეყვანილია 15, დაბეჭდეთ 16.


# user_nuber = int(input("please enter your number: "))
# if user_nuber % 2 == 0:
#     print("your number is even")
# else: 
#     print("your num is not even")
#     print(user_nuber + 1)

# N2
# Create a while loop that asks the user to enter a password. 
# Keep asking until they enter the correct password "Goa best".
# Also print the count of incorrect passwords.

# შექმენით while ციკლი, რომელიც სთხოვს მომხმარებელს პაროლის შეყვანას.
# განაგრძეთ კითხვა, სანამ არ შეიყვანენ სწორ პაროლს "Goa best".
# ასევე დაბეჭდეთ არასწორი პაროლების რაოდენობა.

# correct_password = "goa best"
# registration = "false"

# while registration != True:
#     user_password = input("please enter your password: ")
#     if user_password == correct_password:
#         registration == True
#         print("registration successfully")
#     else:
#         print("password is inccorection")


# N3
# დაწერეთ ალგორითმი, რომელიც მიიღებს სტრიქონს შესაყვანად
# და დააბრუნებს True-ს, თუ ამ სტრიქონის პირველი სიმბოლო არის "G".

# Write an algorithm that takes a string as input and returns
# True if first character of that string is "G".


# best_academy = input("enter the best academy: ")
# if best_academy.startswith("G") and ("g"):
#     print("true")
# else:
#     print("no no no no no no no no no no no")


# N4
# Ask user for five names (use input five times). Add all of them
#  in one list and print only first three names

#სიაში სთხოვეთ მომხმარებელს ხუთი სახელი (გამოიყენეთ შეყვანა ხუთჯერ). 
#დაამატეთ ყველა მათგანი პირველ სიაში და დაბეჭდეთ მხოლოდ პირველი სამი სახელი

# user_names = []
# name1 = input("enter your name1: ")
# name2 = input("enter your name2: ")
# name3 = input("enter your name3: ")
# name4 = input("enter your name4: ")
# name5 = input("enter your name5: ")
# user_names.append(name1)
# user_names.append(name2)
# user_names.append(name3)
# user_names.append(name4)
# user_names.append(name5)

# print(user_names)




# N5
# Write an algorithm that checks if a given number is prime or not
# (prime number has only two divisors - გამყოფი) Use a for loop for this task.

# დაწერეთ ალგორითმი, რომელიც ამოწმებს მოცემული რიცხვს მარტივია თუ არა 
# (მარტივ რიცხვს აქვს მხოლოდ ორი გამყოფი) ამ ამოცანისთვის გამოიყენეთ for loop.

# number = int(input("enter your number: "))
# if number % 2 == 0:
#     print("prime")
# else:
#     print("not prime")


# N6
# Create a while loop that prints numbers from 10 to 0 (10-იდან 0-მდე).

# შექმენით while ციკლი, რომელიც ბეჭდავს რიცხვებს 10-დან 0-მდე (10-დან 0-მდე)

# num = 10
# while num >= 0:
#     print(num)
#     num = num - 1

# N7
# Implement a simple calculator that takes two
# numbers and an operator (+, -, *, /) as input from 
# the user and performs the corresponding operation.
# Bonus task if you want, it's not necessary - add degree (ხარისხი), use ** operator for it.

# განახორციელეთ მარტივი კალკულატორი, რომელიც იღებს ორ რიცხვს და ოპერატორს (+, -, *, /) 
# როგორც შეყვანის სახით მომხმარებლისგან და ასრულებს შესაბამის ოპერაციას.
# ბონუს დავალება თუ გინდა, არ არის საჭირო - დაამატე ხარისხი (ქარი), ამისთვის გამოიყენეთ ** ოპერატორი.

# num1 = int(input("enter first num: "))
# num2 = int(input("enter second num: "))
# operation = (input("enter operation: "))
# for i in num1, num2, operation:
#     if operation == "+":
#         print(num1 + num2)
#     elif operation == "-":
#         print(num1 - num2)
#     elif operation == "*":
#         print(num1 * num2)
#     elif operation == "/":
#         print(num1 / num2)

# N8
#Ask user to enter name and print the last character of that string.

# სთხოვეთ მომხმარებელს შეიყვანოს სახელი და დაბეჭდეთ ამ სტრიქონის ბოლო სიმბოლო.

# name = input("enter your name: ")
# print(name[-1:])

# N9
# Using for loop, ask user for number. Then create a list which will
# have even numbers in next range: from 0 to user's number. At last, print out whole list. 

# loop-ის გამოყენებით, სთხოვეთ მომხმარებელს ნომერი. შემდეგ შექმენით სია,
# რომელსაც ექნება ლუწი რიცხვები შემდეგ დიაპაზონში: 0-დან მომხმარებლის ნომრამდე.
# და ბოლოს, ამობეჭდეთ მთელი სია.


# number = int(input("enter your even number: "))
# even_num = []
# for i in range(number):
#     if i % 2 == 0:
#         even_num.append(i)
# print(even_num)




# N10
# Ask user for whole number.
# Then create a factorial for this number and print it
# out (If you don't know what a factorial is, google it)

# სთხოვეთ მომხმარებელს მთელი ნომერი. 
# შემდეგ შექმენით ფაქტორიალი ამ რიცხვისთვის და ამობეჭდეთ
# (თუ არ იცით რა არის ფაქტორიალი, დაგუგლეთ)


# num = int(input("enter your num: "))
# fact = 1
# for i in range(1,num + 1):
#     fact = fact * i
# print(fact)




