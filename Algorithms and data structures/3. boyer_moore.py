strings = ["test string for MTUCI", "Hello world!", "foo bar"]

def printStrings():
    count = 0
    print("\nДоступные строки:")
    for i in strings:
        count += 1
        print(f"{count}. {i}")

def sensitivitySelection():
    choice = int(input('''
Выбирите вариант чувствительности к регистру:
    1. Чувствительный к регистру.
    2. Нечувствительный к регистру.

Ввод номера: '''))
    return choice

def start():
    action = int(input('''
Укажите номер варианта действия со строками:
    1. Добавить новую строку.
    2. Добавить подстроку в конец существующей строки.
    3. Поиск подстроки в строке.
    4. Получить все доступные строки.

Ввод номера: '''))

    if action == 4:
        return printStrings()
    
    elif action == 1:
        newString = input("Введите строку: ")
        return strings.append(newString)

    elif action == 2:
        printStrings()

        targetString = int(input("\nВведите номер строки: "))
        newSubstring = input("Введите подстроку: ")

        strings[targetString - 1] += newSubstring

        return print(f"\nИзмененная строка: {strings[targetString - 1]}")

    elif action == 3:
        printStrings()
        numTargetString = int(input("\nВведите номер строки: "))
        targetString = strings[numTargetString - 1]
        targetSubstring = input("\nВведите подстроку для поиска: ")
        sensitivity = sensitivitySelection()
        return boyerMooreSearch(targetString, targetSubstring, sensitivity)

        
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

# Алгоритм Бойера-Мура.
def boyerMooreSearch(string, target, sensitivity=1):
    # Случай, если выбрана нечувствительность к регистру.
    if sensitivity == 2:
        string = string.lower()
        target = target.lower()

    # Этап 1: формирование таблицы смещений
    uniqSymbols = set()           # уникальные символы в образе
    numberOfSymbols = len(target) # число символов в образе
    offsets = {}                  # словарь смещений

    for i in range(numberOfSymbols - 2, -1, -1): # итерации с предпоследнего символа
        if target[i] not in uniqSymbols:       # если символ еще не добавлен в таблицу
            offsets[target[i]] = numberOfSymbols - i - 1
            uniqSymbols.add(target[i])

    if target[numberOfSymbols - 1] not in uniqSymbols: # отдельно формируем последний символ
        offsets[target[numberOfSymbols - 1]] = numberOfSymbols

    offsets['*'] = numberOfSymbols                   # смещения для прочих символов

    print(f"\nСмещения: {offsets}")

    # Этап 2: поиск образа в строке
    lenString = len(string)

    if lenString >= numberOfSymbols:
        testSymbol = numberOfSymbols - 1       # счетчик проверяемого символа в строке

        while(testSymbol < lenString):
            k = 0
            j = 0
            flBreak = False
            for j in range(numberOfSymbols - 1, -1, -1):
                if string[testSymbol - k] != target[j]:
                    if j == numberOfSymbols - 1:
                        offset = offsets[string[testSymbol]] if offsets.get(string[testSymbol], False) else offsets['*']  # смещение, если не равен последний символ образа
                    else:
                        offset = offsets[target[j]]   # смещение, если не равен не последний символ образа

                    testSymbol += offset              # смещение счетчика строки
                    flBreak = True                    # если несовпадение символа, то flBreak = True
                    break

                k += 1                                # смещение для сравниваемого символа в строке

            if not flBreak:                           # если дошли до начала образа, значит, все его символы совпали
                print(f"\nПодстрока найдена по индексу {testSymbol - k + 1}")
                break
        else:
            print("\nПодстрока не найдена")

start()

while True:
    stop()

#