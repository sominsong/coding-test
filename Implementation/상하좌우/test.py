#-------------------------------------------------------#
# 난이도 하 / 풀이 시간 15분 / 시간 제한 2초 / 메모리 제한 128 MB
#-------------------------------------------------------#


from cProfile import label
import time
from tracemalloc import start

########################
# 동(R), 서(L), 남(D), 북(U)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direct = {"R":0, "L":1, "D":2, "U":3}

def answer(n, plan):
    x, y = 1, 1 # 현재 위치

    for d in plan:
        nx = x + dx[direct[d]]
        ny = y + dy[direct[d]]
        if nx > n-1 or ny > n-1 or nx < 1 or ny < 1:
            continue
        else:
            x, y = nx, ny

    print(x, y)
########################

# testcase_f = ["testcase1.txt", "testcase2.txt"]
testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        n = int(f.readline().strip()) # Map 크기
        plan = f.readline().split()

    start_time = time.time()
    
    answer(n+1, plan)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)