# N1 
# შექმენით სია, რომელშიც შეიტანთ რიცხვებს 0-იდან 20-ის ჩათვლით
# (ხელით ჩაწერეთ, ციკლის გარეშე), ბოლოს დაპრინტეთ მთლიანი სია.

# Create an array which will include numbers from 0 to 20 
# (write it manually, without loops), then print whole array.

# num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print(num)



# N2
# შექმენით ახალი სია, რომელშიც შეიტანთ ლუწ რიცხვებს წინა სიიდან. ბოლოს დაპრინტეთ ეს სია.
# Create a new array, which will include even
# numbers from the first array. Then print this new array.

# num1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# print(num1)



# N3
# შექმენით ახალი სია, შემდეგ 50-იდან 100-მდე ამ სიაში შეიტანეთ ყველა
# რიცხვი (დასერჩეთ python array append). ბოლოს დაპტინტეთ თქვენთვის
# სასურველი სიის ნაწილი უარყოფითი index-ების საშუალებით.

# Create an array, then add numbers from 50 to 100 to it. In the end,
# print the part of this array with negatives indexes.

# num2 = []
# for i in range(50, 100):
#     num2.append(i)
# print(num2[-6])



# N4
# მომხმარებელს შეეკითხეთ ორი მთელი რიცხვი, შემდეგ ამ ორი
# ცვლადიდან for ციკლში უმცირესი ჩასვის start-ის, ხოლო 
# უდიდესი end-ის პოზიციაზე, step არ გინდათ. ახლა ჩაურთეთ if statement
# და დაპრინტეთ მარტო ხუთის ჯერადები.

# Ask user for two inputs and store them as variables, 
# their type has to be int. Then use for loop, use lower number
#  from this two variables as start, Higher number as end,
# you do not need step. After that, you'll have to use if statement 
# to only print multiples of five.

# num = int(input("enter your first num: "))
# num1 = int(input("enter your second num: "))
# numbers = []
# for i in range(min(num, num1), max(num, num1)):
#     numbers.append(i) 
# for num in numbers:
#     if num % 5 == 0:
#         print(num)



# N5
# შექმენით ახალი სია. შემდეგ მომხმარებელს შეეკითხეთ მისი ასაკი და თუ 
# ასაკი 18-ზე მეტი იქნება, შეეკითხეთ მას სახელი. მეორე ინფუთის
# შემდეგ სახელი შეიტანეთ სიაში და დაპრინტეთ ის.

# Create a new array. Ask user his/her age and if it will be over 18, 
# ask him/her name. Then add this name to already created array and print it.

# my_list = []
# age = int(input("enter your age: "))
# if age > 18:
#     name = (input("enter your name: "))
#     my_list.append(age)
#     my_list.append(name)
# print(my_list)

