# N1

# Greatest common divisor

# Find the greatest common divisor of two positive integers.
# The integers can be large, so you need to find a clever solution.
# The inputs x and y are always greater or equal to 1,
# so the greatest common divisor will always be an integer that is also greater or equal to 1.

# def mygcd(x, y):
#     while y > 0:
#         x, y = y, x % y
        
#     return x


#______________________________________________________________________________________________________


# N2

# Collatz

# A collatz sequence, starting with a positive integern,
# is found by repeatedly applying the following function to n until n == 1 :

# def collatz(n):
#     list = []
#     while n != 1:
#         list.append(int(n))
        
#         if n % 2 == 0:
#             n = n / 2
#         else:
#             n = (n * 3) + 1
#     list.append(1)
    
#     str = ""
#     for i in list:
#         str += f"->{i}"
#     return str[2:]


#______________________________________________________________________________________________________

# N3

# Array plus array

# I'm new to coding and now I want to get the sum of two arrays...
#  Actually the sum of all their elements. I'll appreciate for your help.
# P.S. Each array includes only integer numbers. Output is a number too.

# def array_plus_array(arr1,arr2):
#     result = 0
    
#     for index in range(len(arr1)):
#         result += arr1[index] + arr2[index]
        
#     return result


#_________________________________________________________________________________________________________


# N4

# Rock Paper Scissors!

# Let's play! You have to return which player won! In case of a draw return Draw!.


# def rps(p1, p2):
    
#     if p1 == "scissors" and p2 == "paper":
#         return "Player 1 won!"
#     elif p1 == "paper" and p2 == "rock":
#         return "Player 1 won!"
#     elif p1 == "rock" and p2 == "scissors":
#         return "Player 1 won!"
#     elif p1 == p2:
#         return "Draw!"
#     else: 
#         return "Player 2 won!"


#_________________________________________________________________________________________________________


# N5

# Area or Perimeter

# You are given the length and width of a 4-sided polygon. 
# The polygon can either be a rectangle or a square.
# If it is a square, return its area. If it is a rectangle, return its perimeter.

# def area_or_perimeter(l , w):
#     if l == w:
#         return l * w
#     else:
#         return (l + w) * 2