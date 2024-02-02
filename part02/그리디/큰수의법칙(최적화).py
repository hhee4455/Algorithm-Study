#N,M,K를 공백으로 구분하여 입력받기
n,m,k = map(int,input().split())
#N개의 수를 공백으로 구분하여 입력받기기
data = list(map(int, input().split()))

data.sort(reverse = True) #입력받은 수들 정렬하기
first = data[0]  #가장 큰수
secound = data[1] #두 번째로 큰 수

#가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first #가장 큰 수 더하기
result += (m - count) * secound #두 번째로 큰 수 더하기

print(result)