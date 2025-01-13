n,m = map(int,input().split())
num = []

for _ in range(n):
    array = list(map(int,input().split()))
    num.append(min(array))

max_num = max(num)

print(max_num)