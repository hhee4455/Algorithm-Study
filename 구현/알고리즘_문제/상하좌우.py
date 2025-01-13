n = int(input()) 
input_array = list(input().split())

start = [1, 1]

L = [-1, 0]
R = [1, 0]
U = [0, -1]
D = [0, 1]

for move in input_array:
    if move == 'L':
        dx, dy = L
    elif move == 'R':
        dx, dy = R
    elif move == 'U':
        dx, dy = U
    elif move == 'D':
        dx, dy = D
    else:
        continue 

    if 1 <= start[0] + dx <= n and 1 <= start[1] + dy <= n:
        start[0] += dx
        start[1] += dy

x, y = start
print(y, x)
