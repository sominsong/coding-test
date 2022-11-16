### Bellman Ford 알고리즘 ###
# 조건: 음수 edge가 포함된 그래프에서 최단 경로 찾기
# 원리: 각 Node를 순회하며, 매 Node마다 모든 Edge까지의 거리 업데이트, 이 때 마지막 노드에서도 거리 테이블의 값이 update된다면 음수 cycle 존재한다고 판단함
# Dijkstra와의 차이점: Dijkstra의 경우, 각 Node를 순회하며, 매 Node마다 가장 거리가 짧은 Edge를 선택해서 해당 Node까지의 거리 update

INF = int(1e9)  # 무한을 의미하는 값으로 10억 설정
# 모든 edge 정보 담는 테이블
edges = []

with open("bellman-ford.txt","r") as f:
    # node 개수, edge 개수
    n,m = map(int, f.readline().split())
    # n1, n2, weight
    for _ in range(m):
        a, b, w = map(int, f.readline().split())
        edges.append((a,b,w))
    # 거리 테이블 초기화
    dist = [INF] * (n+1)

def bf(start):
    # 시작 노드 거리 0으로 초기화
    dist[start] = 0
    # 전체 node에 대해 round 반복
    for i in range(n+1):
        # 각 node마다 '모든 edge'까지의 최단 거리 update
        for edge in edges:
            cur,next,cost = edge
            # edge가 존재 & 현재 node를 거쳐갈 때 더 적은 비용일 경우 -> 거리 테이블 update
            if dist[cur] != INF and dist[next] > cost + dist[cur]:
                dist[next] = cost + dist[cur]
                # 마지막 node에서도 update가 된다면, negative cycle 존재
                if i == n-1:
                    return True
    return False

negative_cycle = bf(1)

if negative_cycle:
    print(-1)
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        # 도달할 수 없는 경우 -1 출력
        if dist[i] == INF:
            print(i, ": -1")
        # 도달할 수 있는 경우 거리 출력
        else:
            print(i, ": ", dist[i])


