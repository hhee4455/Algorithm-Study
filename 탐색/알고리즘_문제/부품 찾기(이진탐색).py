def search(array,target,start,end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return target
        elif array[mid] > target:
            end = mid - 1
        else: start = mid + 1
    return None


n = int(input())
n_array = list(map(int,input().split()))
n_array.sort()

m = int(input())
m_array = list(map(int,input().split()))

for i in m_array:
    result = search(n_array,i,0,n-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
