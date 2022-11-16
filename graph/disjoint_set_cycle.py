### 서로소 집합 알고리즘을 이용한 cycle 판별 ###
# 개념: parent가 서로 같을 경우, Cycle이다

# vertex, edge 개수
v, e = 3, 3

# edge List
eList = [(1,2), (1,3), (2,3)]

# parent table 생성 및 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

def find_parent(parent, x):
    # root 노드 찾을 때까지 재귀 호출 + path compression
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

    return parent

cycle = False # cycle 판별 여부

for i in range(e):
    a, b = eList[i]
    # parent가 같으면 cycle
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 다르면 union 수행
    else:
        parent = union_parent(parent, a,b)

if cycle:
    print("yes cycle")
else:
    print("no cycle")