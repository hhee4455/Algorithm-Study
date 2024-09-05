num = list(map(int, input().split()))
m = int(input())

num.sort()

start = 0
end = len(num) - 1
result = 0

while start <= end:
    mid = (start + end) // 2
    if num[mid] == m: 
        result = mid
        break
    elif num[mid] < m:
        start = mid + 1
    else:
        end = mid - 1

print(result)
