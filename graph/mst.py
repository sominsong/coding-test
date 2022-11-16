### Minimum Spanning Tree(MSP) ###
# 원리: cost가 적은 edge 부터 traverse하며 cycle이 없는 경우만 mst에 포함시킴

# vertex, edge 수 
v, e = 7, 9
# edge List (cost, v1, v2)
edges = [(29, 1,2),(75, 1,5),(35, 2,6),(34, 2,6),(7, 3,4),(13, 4,7),(23, 4,6),(53, 5,6),(25, 6,7)]

# parent table 초기화
parent = [0] * (v+1)
for i in range(1, v+1):
    parent[i] = i

def find_parent(parent, x):
    # root 노드 찾을 때까지 재귀
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    return parent

# edge cost로 정렬
edges.sort()

# MST에 포함된 edge들의 총 cost
result = 0

# edge 순회
for edge in edges:
    cost, a, b = edge
    # cycle일 경우에만 MST에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)