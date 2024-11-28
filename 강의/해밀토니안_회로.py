#해밀토니안 알고리즘 만들기
#해밀토니안 알고리즘은 그래프의 모든 정점을 한 번씩 방문하는 알고리즘

def hamiltonian(graph, start, end, visited, path):
    visited[start] = True
    path.append(start)
    if start == end:
        print(path)
    else:
        for i in graph[start]:
            if not visited[i]:
                hamiltonian(graph, i, end, visited, path)
    visited[start] = False
    path.pop()

graph = [[1,2,3],
        [0,2],
        [0,1,3],
        [0,2]]

visited = [False]*4
path = []
hamiltonian(graph, 0, 3, visited, path)