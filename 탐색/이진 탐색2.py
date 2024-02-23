def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end ) // 2
        if array[mid] == target:
            return target
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

input_data = input().split()
n = int(input_data[0])
target = int(input_data[1])
array = list(map(int,input().split()))


print(binary_search(array,target,0,n-1)+1)
