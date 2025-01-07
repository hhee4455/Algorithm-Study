n, k = map(int,input().split())
A_arr = list(map(int,input().split()))
B_arr = list(map(int,input().split()))

A_arr = sorted(A_arr)
B_arr = sorted(B_arr, reverse = True)

for i in range(k):
    if A_arr[i] < B_arr[i]:
        A_arr[i], B_arr[i] = B_arr[i], A_arr[i]
    else:
        break

print(sum(A_arr))