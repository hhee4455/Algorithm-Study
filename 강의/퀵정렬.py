# 퀵정렬 알고리즘
def qck_sort(num_array, pivot, tail):
    if len(num_array) <= 1:
        return num_array
    
    left_partion = [i for i in num_array if i < pivot]
    right_partion = [i for i in num_array if i > pivot]

    if len(left_partion) > 1:
        left_partion = qck_sort(left_partion, left_partion[0], left_partion[-1])
    if len(right_partion) > 1:
        right_partion = qck_sort(right_partion, right_partion[0], right_partion[-1])

    return left_partion + [pivot] + right_partion
    
num_array = list(map(int, input().split()))
pivot = num_array[0]
tail = num_array[-1]
print(qck_sort(num_array, pivot, tail))