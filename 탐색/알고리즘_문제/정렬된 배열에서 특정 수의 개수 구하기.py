n, x = map(int, input().split())
input_array = list(map(int, input().split()))

# 이진 탐색: target 값이 처음 등장하는 인덱스 찾기
def find_first(target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if input_array[mid] == target:
            result = mid
            end = mid - 1  # 더 왼쪽에 target이 있을 수 있으므로 왼쪽을 탐색
        elif input_array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return result

# 이진 탐색: target 값이 마지막 등장하는 인덱스 찾기
def find_last(target, start, end):
    result = -1
    while start <= end:
        mid = (start + end) // 2
        if input_array[mid] == target:
            result = mid
            start = mid + 1  # 더 오른쪽에 target이 있을 수 있으므로 오른쪽을 탐색
        elif input_array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return result

# 첫 번째와 마지막 등장 위치를 찾기
first = find_first(x, 0, n - 1)
if first == -1:
    print(0)  # target이 없으면 0 출력
else:
    last = find_last(x, 0, n - 1)
    print(last - first + 1)  # 개수는 마지막 인덱스 - 첫 번째 인덱스 + 1
