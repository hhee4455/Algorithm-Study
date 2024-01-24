a = [1,2,3,4,5,6,7,8,9]
print(a[0:3])

print(a[4])

a = list(range(0,100,2))
print(a)

a = [1,2,3,4,5,6,7,8,9]
print(a[-1])

a[3] = 7
print(a)

array = [i for i in range(10) if i % 2 == 1] #0~9까지의 수 중 홀수만
print(array)

array = [i*i for i in range(1,10)] #1~9까지의 수 제곱
print(array)

#n*m 크기의 2차원 리스트 초기화
n = 3
m = 4
array = [[0] * m for _ in range(n)] #_는 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 사용 
print(array)


summary = 0
for i in range(1,10):
    summary += i
print(summary)

for _ in range(5):
    print("Hello World")

#잘못된 방법
n = 3
m = 4
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)

#리스트 관련 기타 메서드
# append() #원소 삽입
# sort() #오름차순 정렬
# sort(reverse=True) #내림차순 정렬
# reverse() #원소 뒤집기
# insert(삽입할 위치 인덱스, 삽입할 값) #특정 인덱스 위치에 원소 삽입
# count(특정 값) #특정한 값의 개수
# remove(특정 값) #특정한 값의 원소 제거

a = [1,4,3]
print("기본 리스트: ", a)

#리스트에 원소 삽입
a.append(2)
print("삽입: ", a)

#오름차순 정렬
a.sort()
print("오름차순 정렬: ", a)

#내림차순 정렬
a.sort(reverse=True)
print("내림차순 정렬: ", a)

#리스트 원소 뒤집기
a.reverse()
print("원소 뒤집기: ", a)

#특정 인덱스에 데이터 추가
a.insert(2,3)
print("인덱스 2에 3 추가: ", a)

#특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수: ", a.count(3))

#특정 값 데이터 삭제
a.remove(1)
print("값이 1인 데이터 삭제: ", a)


a = [1,2,3,4,5,5,5]
remove_set = {3,5}

#remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set] #1
print(result)