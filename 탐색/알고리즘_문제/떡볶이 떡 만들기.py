n, m = map(int,input().split())
array = list(map(int,input().split()))

def cut(array, m, start, end):
    array = sorted(array)
    mid = (start + end) // 2
    cut_array = []

    cut_array = [max(0, x - mid) for x in array] 

    total = sum(cut_array)
    
    if total == m:  # 필요한 길이와 정확히 일치하면 반환
        return mid
    elif total > m:  # 떡이 너무 많이 남으면 톱날 높이를 올림
        return cut(array, m, mid + 1, end)
    else:  # 떡이 부족하면 톱날 높이를 내림
        return cut(array, m, start, mid - 1)

start = 0
end = max(array)

print(cut(array, m, start, end))