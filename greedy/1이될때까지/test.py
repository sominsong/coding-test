#-------------------------------------------------------#
# 난이도 하 / 풀이 시간 15분 / 시간 제한 2초 / 메모리 제한 128 MB
# 소요 시간: 5분
#-------------------------------------------------------#

import time
from tracemalloc import start

########################
def answer(N, K):
    cnt = 0
    while True:
        if N == 1:
            break
        if N % K == 0:  # 2 이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 훨씬 많이 줄일 수 있기 때문
            N = N // K
        else:
            N = N - 1
        cnt = cnt + 1
    print(cnt)
########################

########################
def best_answer(N, K):
    result = 0
    while True:
        # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
        target = (N//K) * K
        result += (N - target)
        N = target
        # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
        if N < K:
            break
        # K로 나누기
        result += 1
        N //= K
    
    # 마지막으로 남은 수에 대하여 1씩 뺘기
    result += (N - 1)
    print(result)
########################




testcase_f = ["testcase1.txt", "testcase2.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        N, K = map(int, f.readline().strip().split())

    start_time = time.time()
    
    # answer(N, K)
    best_answer(N, K)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)