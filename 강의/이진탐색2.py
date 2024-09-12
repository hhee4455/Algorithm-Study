def binary_Search(array,n,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == n:
            return mid
        elif array[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    return None

array = list(map(int, input().split()))
n = int(input())
array.sort()

print(binary_Search(array,n,0,len(array)-1)+1)