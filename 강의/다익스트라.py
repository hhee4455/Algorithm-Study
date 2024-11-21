import heapq

def dijkstra(graph, start):
    # 최단 거리 테이블 초기화
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # 우선순위 큐 초기화 (거리, 노드)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 이미 처리된 노드라면 무시
        if current_distance > distances[current_node]:
            continue
        
        # 인접 노드 확인
        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 더 짧은 경로 발견 시 갱신
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(priority_queue, (distance, adjacent))
    
    return distances

# 그래프 예제 (인접 리스트)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 시작 노드 설정
start_node = 'B'
shortest_distances = dijkstra(graph, start_node)

print(f"Shortest distances from node {start_node}: {shortest_distances}")
