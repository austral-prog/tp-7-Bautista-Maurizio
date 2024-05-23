def index_of_by_index(word, list, index):
    for a, element in enumerate(list[index:]):
        if element == word:
            return a + index
    return -1


def index_of_empty(list):
    for index, element in enumerate(list):
        if element == "":
            return index
    return -1


def index_of(word, list):
    for index, element in enumerate(list):
        if element == word:
            return index
    return -1


def put(word, list):
    for index, element in enumerate(list):
        if element == "":
            list[index] = word
            return index
    return -1


def remove(word, list):
    contar = 0
    for index, element in enumerate(list):
        if element == word:
            list[index] = ""
            contar += 1
            print(list)
    return contar
    return -1
