# 선택 알고리즘

def selection_sort(num_array):
    for i in range(len(num_array)):
        min_index = i
        for j in range(i+1, len(num_array)):
            if num_array[min_index] > num_array[j]:
                min_index = j
        num_array[i], num_array[min_index] = num_array[min_index], num_array[i]
    return num_array

num_array = list(map(int, input().split()))
print(selection_sort(num_array))