num = list(input())

num_left = num[:len(num)//2]
num_right = num[len(num)//2:]

num_left_sum = 0
num_right_sum = 0

for i in num_left:
    num_left_sum += int(i)

for i in num_right:
    num_right_sum += int(i)

if num_left_sum == num_right_sum:
    print("LUCKY")
else:
    print("READY")