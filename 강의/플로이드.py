#ployed 코드
def matMult_DP(array, n):
    m = [[0 for i in range(n)] for j in range(n)]
    for d in range(1, n-1):
        for i in range(1, n-d):
            j = i + d
            m[i][j] = 1000000000
            for k in range(i, j):
                m[i][j] = min(m[i][j], m[i][k] + m[k+1][j] + array[i-1]*array[k]*array[j])

    return m[1][n-1]

n = int(input())
array = list(map(int, input().split()))
print(matMult_DP(array, n))