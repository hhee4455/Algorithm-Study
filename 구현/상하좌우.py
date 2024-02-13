n = int(input())
move = input().split()  
m = [[0] * n for _ in range(n)]  
a = 0
b = 0
A = m[a][b]  

for i in range(len(move)):
    if move[i] == 'R':
        if(b == n) : pass
        else : b += 1
    elif move[i] == 'L': 
        if(b == 0): pass
        else : b -= 1
    elif move[i] == 'U': 
        if(a == 0): pass
        else : a -= 1
    elif move[i] == 'D':
        if(a == n): pass
        else : a += 1

print(a+1 ," ", b+1)