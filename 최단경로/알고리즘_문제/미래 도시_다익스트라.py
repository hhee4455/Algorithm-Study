import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
start = 1

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

x, k = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

distance = [INF] * (n+1)
dijkstra(start)
k_dis = distance[k]

distance = [INF] * (n+1)
dijkstra(k)
x_dis = distance[x]

if (k_dis + x_dis) > INF:
    print(-1)
else:
    print(k_dis+x_dis)
