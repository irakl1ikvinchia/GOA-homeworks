# N1

def pig_it(text):
    symbols = ['!', '?']
    words_list = text.split(" ")
    result = []
    
    for word in words_list:
        if word not in symbols:
            result.append(word[1:] + word[0] + "ay")
        else:
            result.append(word)
    
    return " ".join(result)

#_________________________________________________________________________________________________________________


# N2

def pig_it(text):
    symbols = ['!', '?']
    words_list = text.split(" ")
    result = []
    
    for word in words_list:
        if word not in symbols:
            result.append(word[1:] + word[0] + "ay")
        else:
            result.append(word)
    
    return " ".join(result)


#_________________________________________________________________________________________________________________


# N3

# art = books list
# cat = search books list

def stock_list(art, cat):
    if len(art) == 0 or len(cat) == 0:
        return ""
    
    books_amount = {}
    
    for char in cat:
        books_amount[char] = 0
        for book in art:
            if char == book[0]:
                books_amount[char] += int(book.split(" ")[1])
    
    result_str = []
    
    for key in books_amount:
        result_str.append(f"({key} : {books_amount[key]})")
        
    return " - ".join(result_str)
    
#_________________________________________________________________________________________________________________


# N4

def dir_reduc(arr):
    completed_list = []
    opposites = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}

    for i in arr:
        if len(completed_list) != 0 and completed_list[-1] == opposites[i]:
            completed_list.pop() 
        else:
            completed_list.append(i)

    return completed_list

#_________________________________________________________________________________________________________________