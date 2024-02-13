n,m = map(int,input().split())
k = []

for i in range(n):
    data = list(map(int, input().split()))
    data.sort()
    k.append(data[0])
    
k.sort()
print(k[-1])