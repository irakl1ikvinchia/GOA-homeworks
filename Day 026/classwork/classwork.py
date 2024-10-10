# შექმენით პროგრამა, სადაც ბოლოდან პირველ ოთხის ჯერად რიცხვებს გამოიტანთ 
# მაგ სიაში კი 10-დან 50-ის ჩათვლით უნდა იყოს რიცხვები

numbers_list = []

for i in range(10, 50+1):
    numbers_list.append(i)

def find_last_even(numbers):
    for index in range(len(numbers) -1, -1, -1):
        if numbers[index] % 4 == 0:
            return numbers[index]
        
print(find_last_even(numbers_list))