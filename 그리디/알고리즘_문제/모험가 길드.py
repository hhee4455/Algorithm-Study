n = int(input())
input_array = list(map(int, input().split()))

array = sorted(input_array, reverse=True)
count = 0

while array:
    x = array[0]
    if x <= len(array):  # x가 배열 크기 이하일 때만 진행
        array = array[1:len(array)-x+1]
        count += 1
    else:
        break  # x가 배열 크기보다 크면 종료

print(count)
