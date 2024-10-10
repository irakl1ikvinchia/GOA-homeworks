# N1

# Given an unsorted array of 3 positive integers [ n1, n2, n3 ], 
# determine if it is possible to form a Pythagorean Triple using those 3 integers

def pythagorean_triple(integers):
    n1, n2, n3 = sorted(integers)
    c = n3
    
    if n1**2 + n2**2 == c**2:
        return True
    if n1**2 + n3**2 == c**2:
        return True
    if n2**2 + n3**2 == c**2:
        return True
    else:
        return False