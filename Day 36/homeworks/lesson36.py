# N1

# შექმენით ფუნქცია სახელად manual_reverse, 
# რომელიც მიიღებს დალაგებულ კოლექციას.
# თქვენი დავალებაა, რომ შეაბრუნოთ ეს კოლექცია და დააბრუნოთ ამ სახით

# def manual_reverse(number):
#     reversed_numbers = []

#     for i in number():
#         number.reverse()
#         reversed_numbers.append(number)
    
#     return reversed_numbers

# print(manual_reverse([1,2,3,4,5,6]))

#_____________________________________________________________________________________________


# N2

# შექმენით ფუნქცია სახელად manual_replace,
# რომელიც მიიღებს სია, ჩასანაცლებელ ელემენტს და იმ ელემენტს,
# რომლითაც უნდა ჩანაცვლდეს. თქვენი დავალებაა,
# რომ დააბრუნოთ ახალი კოლექცია, სადაც გექნებათ ჩანაცვლებული ყველა ელემენტი მესამე პარამეტრით.

# def manual_replace(lst, old_elem, new_elem):
#     my_list = []
#     for x in lst:
#         if x == old_elem:
#             my_list.append(new_elem)
#         else:
#             my_list.append(x)

#     return my_list 

# print(manual_replace([1,2,3,4,5],3,7))



#___________________________________________________________________________________________________________


# N3

# შექმენით ფუნქცია სახელად manual_count,
# რომელიც მიიღებს დალაგებულ კოლექციას და დასათვლელ მნიშვნელობას.
# თქვენი დავალებაა, რომ დააბრუნოთ თუ რამდენჯერ გექნებათ დასათვლელი მნიშვნელობა კოლექციაში.

# def manual_count(lst,item):
#     count = 0
#     for i in lst:
#         if i == item:
#             count += 1
#     return count

# print(manual_count([1,1,1,2,3,4,5,1], 1))