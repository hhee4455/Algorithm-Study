#분할 정복
def num_half_sorted(num_array):
    mid = len(num_array) // 2

    if len(num_array) == 1:
        return num_array
    else:
        left = num_half_sorted(num_array[:mid])
        right = num_half_sorted(num_array[mid:])

        left.sort()
        right.sort()

        return left + right

num_array = list(map(int, input().split()))
print(num_half_sorted(num_array))