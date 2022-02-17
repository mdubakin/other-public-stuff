matrix = [
    [9, 3, 12, 1],
    [14, 9, 10, 2],
    [21, 64, 32, 8]
]

def bubbleSort(array):
    swapped = False                               # если False сохраняется до конца работы двумерного цикла, то массив отсортирован.   
    for i in range(len(array) - 1, 0, -1):        # перебераем массив с конца
        for j in range(i):                        # перебераем массив от 0 индекса до i (после каждой итерации 1 цикла меняется).
            if array[j] > array[j+1]:             # если элемент больше след. элемента 
                array[j], array[j+1] = array[j+1], array[j] # меняем местами значения элементов.
                swapped = True
        if swapped is True:                       # возвращает значение False и переходим к след. итерации 1-го цикла.
            swapped = False
        else:
            break                                 # если после работы 2-го цикла значение swapped равно False, значит массив отсортирован.
    return array

for index in range(len(matrix)):
    matrix[index] = bubbleSort(matrix[index])

print(matrix)

# Сложность: O(n^2).

# Сложность встроенной функции: O(n log(n))
# matrix[0].sort()
# print(matrix)