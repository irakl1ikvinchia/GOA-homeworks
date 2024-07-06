# N1

# შექმენით პროგრამა სადაც გექნებათ მოცემული სია,
# და უნდა დათვალოთ ამ სიაში ლუწი რიცხვები

# def count_evens(numbers_list):
#     count = 0

#     for number in numbers_list:
#         if number % 2 == 0:
#             count = count + 1

#     return count

# print(count_evens([1,3,4,5,6,7,8,23,14,44]))


# N2

# შექმენით პროგრამა სადაც გექნებათ მოცემული სტრინგი,
# ხოლო ლუწ ინდექსებზე მყოფი ელემენტი ჩაანაცვლეთ სხვა ელემენტით 

# def replaca_even_indexes(word, replace_char):
#     changed_word = ""

#     for index in range(len(word)):
#         if index % 2 == 0:
#             changed_word = changed_word + replace_char
#         else:
#             changed_word = changed_word + word[index]

#     return changed_word

# print(replaca_even_indexes("anmier", "p"))


# N3

# იპოვეთ სიაში ბოლო ლუწი რიცხვის ინდექსი

# def find_last_even(number_list):
#     for i in range(len(number_list) -1, -1, -1):
#         if number_list[i] % 2 == 0:
#             return i
        
# print(find_last_even([1,2,3,4,5,6,7,11,9]))


