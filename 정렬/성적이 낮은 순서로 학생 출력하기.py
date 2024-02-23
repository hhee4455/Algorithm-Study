n = int(input())

m = [list(input().split()) for _ in range(n)] 

m = sorted(m)

for i in range(n):
    print(m[i][0], end= ' ')