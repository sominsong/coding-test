### Floyd-Warshall 알고리즘 ###
# a-b 보다 a-k-b가 더 짧은지 비교하는 알고리즘

INF = int(1e9) # 무한 = 10억

# 노드의 개수, 간선의 개수
n,m = 4, 7
# 각 노드에 연결되어 있는 노드에 대한 정보를 담기 위한 2차원 배열 선언
graph = [[INF] * (n+1) for _ in range(n+1)]
# 자기 자신은 0으로 초기화
for i in range(1, n+1):
    graph[i][i] = 0

# 각 edge에 대한 정보 받기
graph[1][2] = 4
graph[1][4] = 6
graph[2][1] = 3
graph[2][3] = 7
graph[3][1] = 5
graph[3][4] = 4
graph[4][3] = 2

# 점화식에 따라 Floyd-Warshall 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            # 점화식 수행
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            continue
        else:
            print(a, b, ": ", graph[a][b])