def fibo_dp(num):
    num[0] = 0
    num[1] = 1

    for i in range(2, len(num)):
        num[i] = num[i - 1] + num[i - 2]
    return num[len(num) - 1]    

num = int(input())
num = [0] * (num + 1)
print(fibo_dp(num))