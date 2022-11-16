#-------------------------------------------------------#
# 난이도 상 / 풀이 시간 60분 / 시간 제한 1초 / 메모리 제한 128 MB
# 소요 시간: 분
# 정답 여부: 
# Key Idea: 한 도시에서 다른 도시까지의 최단 거리 문제 (N,M의 범위가 충분히 큼 -> 우선순위 큐를 활용한 다익스트라 알고리즘 구현)
#-------------------------------------------------------#

import time
from tracemalloc import start

# Min Heap 이용
import heapq
# Infinite 정의
INF = int(1e9)

########################
# Dijkstra 알고리즘: 한 노드에서 다른 모든 노드까지의 최단 거리
def answer(n,m,start, graph):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    visited = set()

    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리되었으면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            # 거쳐 가는 경우
            cost = dist + i[1]
            # 현재 최소 거리보다 거쳐가는게 더 짧을 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                # 방문 노드 기록
                visited.add(i[0])

    # 메세지를 받는 도시의 총 개수
    print(len(visited), end=' ')
    # 총 걸리는 시간 
    except_INF = list(set(distance) - {INF})
    except_INF.sort(reverse=True)
    print(except_INF[0])
########################


testcase_f = ["testcase1.txt", "testcase2.txt"]
# testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        n, m, start= map(int, f.readline().split())
        graph = [[]for i in range(n+1)]
        distance = [INF]*(n+1)

        for _ in range(m):
            x, y, z = map(int, f.readline().split())
            graph[x].append((y,z))

    start_time = time.time()
    
    answer(n,m,start, graph)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)