n,k = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(2)]

array[0].sort()
array[1].sort(reverse=True)

for i in range(k):
    if array[0][i] >= array[1][i]:
        break
    else:
        array[0][i], array[1][i] = array[1][i], array[0][i]
    
print(sum(array[0]))