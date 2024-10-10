geese = ["African", "Roman Tuted", "Toulouse", "piligrim", "steinbacher"]
def goose_filter(birds):
    filtered_list = []

    for bird in birds:
        if bird not in geese:
            filtered_list.append(bird)

    return filtered_list