matrix = [
    [9, 3, 12, 1],
    [14, 9, 10, 2],
    [21, 64, 32, 8]
]

def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

for index in range(len(matrix)):
    matrix[index] = quickSort(matrix[index])

print(matrix)

# Сложность: O(n^2)