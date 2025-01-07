array = [3,1,2,6,7,4,3]

for i in range(len(array)):
    min = i
    for j in range(i+1, len(array)):
        if array[min] > array[j]:
            min = j
    array[i], array[min] = array[min], array[i]

print(array)