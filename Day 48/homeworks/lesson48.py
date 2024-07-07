# N1

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    min_sum = numbers[0] + numbers[1]
    
    return min_sum

#_____________________________________________________________________________________________________________

# N2

def get_even_numbers(arr):
    even_num = []
    for i in arr:
        if i % 2 == 0:
            even_num.append(i)
            
    return even_num

#_____________________________________________________________________________________________________________