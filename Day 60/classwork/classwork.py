#N1

# def reverse_number(n):
#     n = str(n)
#     n = n[::-1]
    
#     if n[-1] == '-':
#         n = n[0:-1]
#         n = "-" + n
        
    
#     return int(n)
#_______________________________________________________________________________________________________

#N2

# def find_average(numbers):
#     if len(numbers) == 0:
#         return 0
    
#     sum_of_numbers = sum(numbers)
#     length_of_numbers = len(numbers)
    
#     return sum_of_numbers / length_of_numbers

#_______________________________________________________________________________________________________

#N3

# def vaporcode(s):
#     s = s.replace(" ", "")
#     s = s.upper()
#     chars = []
    
#     for char in s:
#         chars.append(char)
    
#     return "  ".join(chars)

#______________________________________________________________________________________________________

#N4

# def length_of_sequence(arr,n):
#     if arr.count(n) != 2:
#         return 0
    
#     first = arr.index(n)
#     second = arr.index(n, first + 1)
    
#     return second - first + 1

#_______________________________________________________________________________________________________

#N5

# def tail_swap(strings):
#     first_arr = strings[0].split(':')
#     second_arr = strings[1].split(':')
    
    
#     temp = first_arr[1]
#     first_arr[1] = second_arr[1]
#     second_arr[1] = temp
    
    
#     return [":".join(first_arr), ":".join(second_arr)]

#_______________________________________________________________________________________________________

#N6



#_______________________________________________________________________________________________________