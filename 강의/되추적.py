#promising 알고리즘
#1. 현재 위치에서 출구까지 가는 경로가 존재하면
#2. 현재 위치에서 출구까지 가는 경로가 없는 경우
#3. 현재 위치가 출구인 경우

def findpath(x,y):
    if x<0 or y<0 or x>=N or y>=N:
        return False
    elif maze[x][y] == 3:
        return True
    elif maze[x][y] == 1:
        maze[x][y] = 7
        if findpath(x,y-1) or findpath(x,y+1) or findpath(x-1,y) or findpath(x+1,y):
            return True
        return False
    else:
        return False

N = 5
maze = [[1,1,1,1,1],
        [1,0,0,0,1],
        [1,1,1,0,1],
        [1,0,0,0,1],
        [1,1,1,3,1]]
print(findpath(1,1))