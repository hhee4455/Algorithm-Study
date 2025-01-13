n = input()

x,y = list(n) 
x = ord(x)- 96
y = int(y)

count = 0

move_knight = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

for move in move_knight:
    nx = x + move[0]
    ny = y + move[1]

    if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
        continue
    else:
        count += 1

print(count)