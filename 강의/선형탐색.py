num = list(map(int,input().split()))

num.sort()
max = num[-1]

print(max)


max_2 = 0

for i in range(1, len(num)):
    if num[i] > num[i-1]:
        max_2 = num[i]
    else:
        continue

print(max_2)