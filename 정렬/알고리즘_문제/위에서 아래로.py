n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

# 1번 방법
array.sort(reverse = True)

# 2번 방법
array = sorted(array, reverse=True)

print(array)