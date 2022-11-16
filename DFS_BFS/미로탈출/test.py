#-------------------------------------------------------#
# 난이도 중하 / 풀이 시간 30분 / 시간 제한 1초 / 메모리 제한 128 MB
# 소요 시간: 28분
# 정답 여부: X
# Key Idea: BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색함
#           상하 좌우로의 모든 노드의 거리가 1로 동일함
#           따라서 (1,1)부터 BFS를 수행하여 모든 노드의 최단 거리 값을 기록하면 해결 가능
#-------------------------------------------------------#

import time
from tracemalloc import start

########################
dx = [1,0,-1,0]
dy = [0,1,0,-1]
min = 0

def dfs(maze, n,m, x,y, stack):
    global dx, dy, min
    for d in range(4):
        next_x = x + dx[d]
        next_y = y + dy[d]
        if next_x == m-1 and next_y == n-1:
            stack.append((next_y,next_x))
            if min > len(stack):
                min = len(stack)
        if next_x >= 0 and next_x < m and next_y >= 0 and next_y < n:
            if maze[next_y][next_x] == 1:
                stack.append((next_y, next_x))
                maze[next_y][next_x] = 0
                dfs(maze, n,m,next_x, next_y, stack)
    
def answer(maze, n, m):
    x = 0
    y = 0
    result = 1
    stack = [(0,0)]
    maze[0][0] = 0
    global min 
    min = n*m+1
    # DFS
    path = dfs(maze, n,m, x,y, stack)
    print(min)
########################

########################
from collections import deque
# BFS를 수행한 결과
def best_answer(x, y):
    global maze, dx, dy
    # Queue 구현
    queue = deque()
    queue.append((x,y))
    # Queue가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if maze[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return maze[n-1][m-1]
########################

# testcase_f = ["testcase1.txt", "testcase2.txt"]
testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        n,m = map(int, f.readline().strip().split())
        maze = []
        for i in range(n):
            maze.append(list(map(int, f.readline().strip())))

    start_time = time.time()
    
    # answer(maze, n, m)
    print(best_answer(0,0))
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)