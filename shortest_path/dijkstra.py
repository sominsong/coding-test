### Dijkstra 알고리즘 (Priority Queue, Heap 이용)###
# 하나의 노드에서 다른 노드까지의 최단 경로를 구함
import heapq

INF = int(1e9) # 무한 = 10억

# 노드의 개수, 간선의 개수
n,m = 6, 11
# 시작 노드 변호
start = 1
# 각 노드에 연결되어 있는 노드에 대한 정보를 담기 위한 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력
graph[1].append((2,2))
graph[1].append((4,1))
graph[1].append((3,5))
graph[2].append((3,3))
graph[2].append((4,2))
graph[3].append((2,3))
graph[3].append((6,5))
graph[4].append((3,3))
graph[4].append((5,1))
graph[5].append((3,1))
graph[5].append((6,2))

def dijkstra(start):
    q = []  # priority queue
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:    # 큐가 비어있지 않다면
        # queue에서 꺼내기 (가장 거리가 짧은 것부터)
        dist, now = heapq.heappop(q)
        # 방문 확인 (현재 distance가 queue에서 꺼낸 것보다 짧은지)
        if distance[now] < dist:
            continue    # 방문한 것임
        # 인접 노드 순회
        for i in graph[now]:
            # now를 거쳐 가는 길이 계산
            cost = dist + i[1]
            # 인접 노드의 현재 값보다 now를 거쳐 가는 것이 더 짧다면 update
            if distance[i[0]] > cost:
                # distance 업데이트
                distance[i[0]] = cost
                # queue 업데이트
                heapq.heappush(q, (cost, i[0]))

# 알고리즘 시작    
dijkstra(start)

# 가장 짧은 경로 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print(i, ": INFINITY")
    else:
        print(i, ": ", distance[i]) # 0,2,3,1,2,4
