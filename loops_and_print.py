def enumerate_list(list):
    New_list1 = []
    a = list.count("")
    while a >= 1:
        list.remove("")
        a= list.count("")

    if a == 0:
        for index in range(len(list)):
            New_list1.append(f"{index}. {list[index]}")
        return New_list1






def enumerate_backwards(list):
    New_list1 = []
    New_list2 = []
    a = list.count("")
    while a >= 1:
        list.remove("")
        a = list.count("")

    if a == 0:
        for b in list:
            New_list1.append(b[::-1])
        for item, b in enumerate(New_list1[0:]):
            New_list2.append(f"{item}. {b}")
        return New_list2
