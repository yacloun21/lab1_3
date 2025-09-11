from lib import find


def test_find():
   #  общие элементы есть
    list1 = [1, 2, 3, 4, 6]
    list2 = [3, 4, 5, 6, 7]
    list3 = [5, 6, 7, 8, 9]
    result = find(list1, list2, list3)
    if result == 1:
        print(f"получено {result}")
        print("Тест 1 пройден: три списка")
   #  два списка
    result = find(list1, list2)
    if result == 3:
        print(f"получено {result}")
        print("Тест 2 пройден: два списка ")
    # один список
    result = find(list1)
    if result == 5:
        print(f"получено {result}")
        print("Тест 3 пройден: один список")
    # нет общих элементов
    list4 = [10, 11, 12]
    list5 = [13, 14, 15]
    result = find(list4, list5)
    if result == 0:
        print("Тест 4 пройден: нет общих элементов")
    print("Тесты успешно пройдены")


find()