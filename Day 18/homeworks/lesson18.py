# N1
# შექმენით ფუნქცია, რომელსაც გადაეცემა 1-იდან 20-ის ჩათვლით რიცხვების სია.
# თქვენ უნდა დააბრუნოთ გაფილტრული სია, სადაც უკვე მარტო 4-ის ჯერადები იქნება.

# def sum_of_numbers(numbers):
#     result = []
#     for num in numbers:
#         if num % 4 == 0:
#             result.append(num)
#     return result
        
# nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(sum_of_numbers(nums))


# N2
# შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლისგან მიღებულ სახელსა და გვარს.
# შემდეგ ისინი დაამატეთ სიაში და დააბრუნეთ სია.

# def user_info(name,lastname):
#     user_info_list = []
#     for info in name,lastname:
#         user_info_list.append(info)

#     return user_info_list

# name = input("enter your name: ")
# lastname = input("enter your lastname: ")

# print(user_info(name,lastname))


# N3
# მომხმარებელს შეეკითხეთ საწყისი და საბოლოო რიცხვები.
# ეს რიცხვები გადაეცით ფუნქციას, for ციკლით სიაში შეინახეთ მათ შორის არსებული რიცხვები.
#  შემდეგ მოახდინეთ გაფილტვრა, ისევ for ციკლით განიხილეთ თითოეული რიცხვი
#  - თუ რიცხვი ლუწი იქნება, ახალ სიაში დაამატეთ მისი მეორე ხარისხი,
# ხოლო თუ კენტი იქნება სიაში დაამატეთ მისი კვადრატული ფესვი (0.5 ხარისხი).

# def filter_arr(start_num,end_num):
#     numbers = []
#     filtered_list = []
#     for i in range(start_num,end_num):
#         numbers.append(i)

#     print(numbers)

#     for i in numbers:
#         if i % 2 == 0:
#             filtered_list.append(i ** 2)
#         else:
#             filtered_list.append(i ** 0.5)

#     return filtered_list

# start_num = int(input("enter your start num: "))
# end_num = int(input("enter your end num: "))

# result_list = filter_arr(start_num,end_num)

# print(result_list)


# N4
# შექმენით ფუნქცია, რომელსაც გადასცემთ მომხმარებლის გვარს.
# გვარის თითოეული ასო გადაიტანეთ ახალ სიაში.
# შემდეგ for ციკლის გამოყენებით იმუშავეთ ამ სიაზე 
# - მარტო ლუწ ინდექსებზე მყოფი ასოები დაამატეთ ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია.

# def even_indexes(lastname):
#     char_list = []
#     even_index_char = []

#     for char in lastname:
#      char_list.append(char)
    
#     for index in range(len(char_list)):
#         if index % 2 == 0:
#            even_index_char.append(char_list[index])

#     print(even_index_char)

# lastname = input("enter your lastname: ")

# even_indexes(lastname)

# N5
# შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია.
# თქვენ უნდა დააბრუნოთ ამ სიის საშუალო არითმეტიკული ( ჯამი / სიგრძე )

# def numbers_list(number):
#     print(sum(number) // len(number))

# numbers_list([1,2,3,4,5,6,7,8,9,12,34,546])
    
# N6
# შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლისგან სიტყვას.
# შემდეგ თქვენ უნდა მოახდინოთ ამ სიტყვის შებრუნება, მაგ: word - drow. საბოლოდ კი დააბრუნეთ შედეგი.


# def reversed_string(text):
#     if len(text) == 1:
#         return text
#     return reversed_string(text[1:]) + text[:1]

# print(reversed_string(input("enter your text: ")))


# N7
# შექმენით ფუნქცია, რომელიც მიიღებს რიცხვების
# სიას და თქვენ დააბრუნებთ მის გაფილტრულ ვერსიას,
# რომელსაც არ ექნება დუპლიკატები (ერთი და იგივე ელემენტები)

# def user_number(numbers):
#     print(list(set(numbers)))
    

# user_number([1,3,4,5,2,3,2,5,])

            
    
    





