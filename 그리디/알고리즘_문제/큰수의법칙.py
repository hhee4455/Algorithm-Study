n, m, k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
first = array[-1]    # 가장 큰 수
second = array[-2]   # 두 번째로 큰 수

# 패턴 기반 합산 횟수 계산
count = m // (k + 1) * k  # 가장 큰 수가 더해지는 횟수
count += m % (k + 1)      # 나머지로 가장 큰 수 더하기

# 결과 계산
result = count * first    # 가장 큰 수의 총합
result += (m - count) * second  # 두 번째 큰 수의 총합

print(result)
