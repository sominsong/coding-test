### Disjoint Set ###

# Node 개수와 Edge(Union 연산) 개수 입력 받기
v, e = 6, 4
eList=  [(1,4),(2,3),(2,4),(5,6)]

# parent table 만들기
parent = [0]* (v+1)

# 자기 자신을 parent로 parent table 초기화
for i in range(1, v+1):
    parent[i] = i

def find_parent(parent, x):
    # root 노드를 찾을 때 까지 재귀호출 + path compression
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

# edge (union 연산) 수 만큼 수행
for i in range(e):
    a, b = eList[i]
    parent = union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end= "")
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')

print()

# parent table 출력
print('부모 테이블: ', end='')
for i in range(1, v+1):
    print("(",i, parent[i],")", end='')