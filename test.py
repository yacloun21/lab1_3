from lib import find


def test_find():


    print("Запуск тестов для функции find_common_elements...")

  # Тест 1: Общие элементы есть
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [5, 6, 7, 8, 9]

    result = find(list1, list2, list3)
    if result == 1:
        print(f"Ожидалось 1, получено {result}")
        print("Тест 1 пройден: три списка с одним общим элементом")


   # Тест 2: Два списка
    result = find(list1, list2)
    if result == 3:
        print(f"Ожидалось 3, получено {result}")
        print("Тест 2 пройден: два списка с тремя общими элементами")

    # Тест 3: Один список
    result = find(list1)
    if result == 5:
        print(f"Ожидалось 5, получено {result}")
        print("Тест 3 пройден: один список")

    # Тест 4: Нет общих элементов
    list4 = [10, 11, 12]
    list5 = [13, 14, 15]

    result = find(list4, list5)
    if result == 0:
        print(f"Ожидалось 0, получено {result}")
        print("Тест 4 пройден: нет общих элементов")


    print("Все тесты успешно пройдены")


find()