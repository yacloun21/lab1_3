def find(*lists):

    if len(lists) == 0:
        return 0

    obshee = set(lists[0])
    print(obshee)
    for i in lists[1:]:
        obshee = obshee.intersection(set(i))

    return len(obshee)

list1 = [1, 2, 3, 6, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

result = find(list1, list2, list3)
print(f"Количество одинаковых элементов в трех списках: {result}")

#