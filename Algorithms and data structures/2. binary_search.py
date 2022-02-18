from random import randint

# Получаем массив из 100 случайных целых чисел в промежутке от 0 до 99 включительно.
array = [randint(0, 100) for i in range(100)]

# Сортируем полученный массив.
array.sort()

# ----- Функции ----- #

# Основная функция.
def start():
    action = int(input('''
Укажите номер варианта действия с массивом:
    1. Добавить число в конец массива.
    2. Удалить число из массива.
    3. Поиск индекса числа в массиве.
    4. Вывести массив.

Ввод номера: '''))
    if action == 4:
        return print("\nМассив:", array)

    number = int(input("Введите число: "))

    if action == 1:
        array.append(number)
        print("\nЧисло", number, "добавлено в конец массива.\n", "\nИзмененный массив:", array)

    elif action == 2:
        index = binary_search(array, number)
        if number in array:
            array.pop(index)
            print("\nЧисло", number, "имело индекс", index, "и было удалено из массива.\n", "\nИзмененный массив:", array)
        else:
            print("\n!!! Такого числа нет, попробуйте другое. !!!")

    elif action == 3:
        print("\nИндекс:", binary_search(array, number))

# Функция для завершения или продолжения работы программы.
def stop():
    answer = int(input('''
Закрыть программу или выполнить другое действие:
    1. Закрыть программу.
    2. Выполнить другое действие.
    
Ввод номера: '''))
    if answer == 2:
        start()
    else:
        exit(0)

# Алгоритм бинарного поиска.
def binary_search(array, number):
    low = 0
    high = len(array) - 1
    # count = 0

    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        # count += 1

        if guess == number:
            # return mid, count
            return mid

        elif guess < number:
            low = mid + 1
        
        else:
            high = mid - 1

# ----- Основная логика ----- #

# Запустим программу.
start()

# Программа будет работать до тех пор, пока пользователь не захочет закрыть ее.
while True:
    stop()

# ----- Сложность алгоритма ----- #
# Сложность алгоритма бинарного поиска - O(log2(n))
# Сложность алгоритма поиска встроенного метода index() - O(n). Source: https://blog.finxter.com/python-list-index/ 