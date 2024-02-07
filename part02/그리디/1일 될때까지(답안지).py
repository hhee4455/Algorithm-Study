n, k = map(int,input().split())
count = 0

#n이 k 이상이라면 K로 계속 나누기
while n >= k:
    #n이 k로 나누어 떨아지지 않는다면 N에서 1씩 빼기
    while n % k != 0:
        n -= 1
        count += 1
    #K로 나누기
    n //= k
    count += 1

#마지막으로 남은 수에 대하여 1씩 빼기
while n > 1:
    n -= 1
    count += 1

print(count)


while True:
    #(n == n로 나누어 떨어지는 수)가 될 때까지 1씩 빼기
    target = (n // k) * k
    count += (n-target)
    n = target
    #n이 n보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    count += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
count += (n-1)
print(count)