#-------------------------------------------------------#
# 난이도 중 / 풀이 시간 30분 / 시간 제한 1초 / 메모리 제한 128 MB
# 소요 시간: 35분
# 정답 여부: X
# Key Idea: a_i를 i번째까지 창고의 최적의 식량의 해라고 한다면, k_i가 선택되는 경우는 a_(i-1)보다 a_(i-2)+k_i가 큰 경우이다.
#           점화식은 다음과 같다: a_i = max(a_(i-1), a_(i_2)+k_i)
#-------------------------------------------------------#

import time
from tracemalloc import start


########################
def answer(num, cargo, visited):
    result = 0

    q = list()
    for i, elm in enumerate(cargo):
        q.append((elm, i))
    
    q.sort()

    while q:
        elm, idx = q.pop()
        if visited[idx+1] == False and visited[idx-1] == False:
            result += elm
            visited[idx] = True
        else:
            continue

    print(result)
########################

########################
def best_answer(num, cargo):
    # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
    d= [0]*100

    # 다이나믹 프로그래밍 진행 (Bottom-Up)
    d[0] = cargo[0]
    d[1] = max(cargo[0],cargo[1])
    for i in range(2, num):
        d[i] = max(d[i-1], d[i-2] + cargo[i])

    # 계산된 결과 출력
    print(d[num-1])
########################

testcase_f = ["testcase1.txt", "testcase2.txt"]
# testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        num = int(f.readline())
        cargo = list(map(int, f.readline().split()))
    visited = [False] * (num+1)
    start_time = time.time()
    
    # answer(num, cargo, visited)
    best_answer(num, cargo)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)