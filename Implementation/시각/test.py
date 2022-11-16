#-------------------------------------------------------#
# 난이도 하 / 풀이 시간 15분 / 시간 제한 2초 / 메모리 제한 128 MB
# 소요 시간: 10분
# Key Idea: 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제 (Brute Forcing, 완전 탐색), 단순히 시각을 1씩 증가시키며 3이 포함되어 있는지 확인
#-------------------------------------------------------#

import time
from tracemalloc import start

########################
def answer(N):
    # second = 15
    # minute = 15 * 60
    # hour = n * 60 * 60
    result = 0
    one_hour = 15 * 60 + 60 * 15 - 15 * 15
    for n in range(N, -1, -1):
        if n == 3 or n == 13 or n == 23:
            result = result + (60*60)
        else:
            result += one_hour

    print(result)
########################  

########################  
def best_answer(N):
    result = 0
    for i in range(N+1):
        for j in range(60):
            for k in range(60):
                # 매 시각 안에 3이 포함되어 있다면 카운트 증가
                if '3' in str(i) + str(j) + str(k):
                    result += 1
    print(result)

# testcase_f = ["testcase1.txt", "testcase2.txt"]
testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        N = int(f.readline().strip())

    start_time = time.time()
    
    # answer(N)
    best_answer(N)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)