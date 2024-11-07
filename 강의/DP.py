def cutRod_DP(p, n):
    r = [0]*(n+1)
    for j in range(1, n+1): # 1부터 n까지
        q = -1 # 최대값을 찾기 위해 음수로 초기화
        for i in range(1, j+1): # 1부터 j까지 (j는 n까지)
            q = max(q, p[i] + r[j-i])
        r[j] = q
    return r[n]

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n = int(input())

print(cutRod_DP(p, n))