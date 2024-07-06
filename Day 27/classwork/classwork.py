def longest(a1, a2):
    whole_str = a1 + a2
    sort_list = []
    result = ""

    for char in whole_str:
        if char not in sort_list:
            sort_list.append(char)

    sort_list.sort()

    return "".join(sort_list)