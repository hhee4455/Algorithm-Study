n = int(input())
a = sorted(map(int, input().split()))  # 정렬된 리스트

m = int(input())
b = list(map(int, input().split()))

def binary_search(array, target, start, end):
    if start > end:  # 종료 조건
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] < target:
        return binary_search(array, target, mid+1, end)
    else:
        return binary_search(array, target, start, mid-1)

for target in b:
    if binary_search(a, target, 0, len(a)-1):
        print('yes', end=' ')
    else:
        print('no', end=' ')
