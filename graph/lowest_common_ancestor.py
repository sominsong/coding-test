### 기본적인 O(MlogN) 시간 복잡도 LCA 알고리즘 ###
# M: LCA query 개수
# N: node 개수

# node 개수
n = 15

parent = [0] * (n+1) # parent 정보
visitied = [False] * (n+1) # 방문 정보
d = [0] * (n+1) # depth 정보

graph = [[] for _ in range(n+1)] # graph 정보

# input 저장용 리스트
input = [(1,2),(1,3),(2,4),(2,5),(3,6),(3,7),(4,8),(4,9),(5,10),(5,11),(7,12),(7,13),(11,14),(11,15)]

# graph 생성
for i in range(n-1):
    graph[input[i][0]].append(input[i][1])
    graph[input[i][1]].append(input[i][0])

# root 노드부터 시작해서 depth를 구하는 함수
def dfs(x, depth):
    # 방문 처리
    visitied[x] = True
    # depth 기록
    d[x] = depth
    # 연결된 child 노드로 방문
    for child in graph[x]:
        # 이미 방문한 노드의 경우 skip
        if visitied[child]:
            continue
        # parent 정보 기록
        parent[child] = x
        dfs(child, d[x]+1)

# A와 B의 공통 조상을 찾는 함수
def lca(a, b):
    # 시작 지점 높이 같게 만들기
    while d[a] != d[b]:
        # 둘 중 큰 쪽이 parent로 한 칸 올라가기
        if d[a] > d[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 시작 지점 같아졌으면, common ancestor 찾아서 한 칸씩 올라가기
    while a != b:
        a = parent[a]
        b = parent[b]
    # common ancestor 반환
    return a

# graph의 depth 구하기
dfs(1, 0)   # root 노드 = 1번 노드

# 공통 조상 찾기 input
m = 3
#          2        1       3
input = [(8,14), (10,13), (6,13)]

for i in range(m):
    a, b = input[i]
    print(a,b,lca(a,b))



# node 개수 
n = 15
# LOG height 구하기
LOG = 3 # 2^4 = 16

parent = [[0] * LOG for _ in range(n+1)]  # parent 정보
d = [0] * (n+1) # 각 노드의 depth 정보
visited = [False] * (n+1)   # 방문 기록 정보
graph = [[] for _ in range(n+1)]  # graph 정보

# input 저장용 리스트
input = [(1,2),(1,3),(2,4),(2,5),(3,6),(3,7),(4,8),(4,9),(5,10),(5,11),(7,12),(7,13),(11,14),(11,15)]

# graph 생성
for i in range(n-1):
    a,b = input[i]
    graph[a].append(b)
    graph[b].append(a)

# root 노드부터 시작해서 모든 노드의 depth 구하는 함수
def dfs(x, depth):
    # 방문 표시
    visited[x] = True
    # depth 저장
    d[x] = depth
    # child 노드 방문
    for child in graph[x]:
        # 이미 방문한 적 있다면, skip
        if visited[child]:
            continue
        # parent-child 관계 기록
        parent[child][0] = x
        dfs(child, depth+1)

# 모든 노드의 2^i번째 parent 추가 저장
def set_parent():
    # 모든 노드의 깊이 구하기 & 직계 부모 구하기
    dfs(1, 0)
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

# a, b의 lca 찾는 함수
def lca(a,b):
    # b가 더 깊은 위치에 있는 노드가 되도록
    if d[a] > d[b]:
        a,b = b,a
    # b를 a 높이 만큼 2^i씩 올리기
    for i in range(LOG-1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    # lca라면 반환
    if a == b:
        return a
    # a,b 같이 2^i만큼 올라가면서 lca 차지
    for i in range(LOG-1, -1, -1):
        # 2^i번째 ancestor가 같지 않다면, 해당 ancestor로 이동
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # lca 반환
    return parent[a][0]


# 모든 노드의 2^i번째 부모 구하기
set_parent()

# LCA 찾기
m = 3
#          2        1       3
input = [(8,14), (10,13), (6,13)]

for i in range(m):
    a, b = input[i]
    print(a,b,lca(a,b))


""" parent 출력
for i in range(n+1):
    print(i, end=": ")
    for j in range(LOG):
        print(parent[i][j], end=' ')
    print()
"""