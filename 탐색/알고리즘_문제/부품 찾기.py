def search(n,target,array):
    for i in range(n):
        if n_array[i] == target:
            return 1

n = int(input())
n_array = list(map(int,input().split()))

m = int(input())
m_array = list(map(int,input().split()))

for i in range(m):
    k = search(n,m_array[i],n_array)
    if k == 1:
        print('yes', end = ' ')
    else: print('no', end = ' ')


