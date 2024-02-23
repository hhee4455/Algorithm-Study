def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
input_data = input().split()
n = int(input_data[0])
target = int(input_data[1])
array = list(map(int,input().split()))


print(binary_search(array,target,0,n-1)+1)
