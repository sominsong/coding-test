#-------------------------------------------------------#
# 난이도 하 / 풀이 시간 30분 / 시간 제한 1초 / 메모리 제한 128 MB
# 소요 시간: 30분
# Key Idea: 앞에서부터 공포도를 하나씩 확인하며, '현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도보다 크거나 같다면 이를 그룹으로 설정'
# 정당성: 공포도가 오름차수능로 정렬되어 있다는 점에서, 항상 최소한의 모험가 수만 포함하여 그룹을 결성하게 됨
#-------------------------------------------------------#

import time
from tracemalloc import start

########################
def answer(N, group):
    
    group = sorted(group, reverse =True)

    N = group[0]
    result = 1

    for i in group[1:]:
        if N > 1:
            N -= 1
        else:
            N = i
            result += 1
    if N > 1:
        result -= 1
    
    print(result) 

########################

########################
def best_answer(N, group):
    group = sorted(group)

    result = 0 # 총 그룹의 수
    count = 0 # 현재 그룹에 포함된 모험가의 수
    
    for i in group: # 공포도를 낮은 것부터 하나씩 확인하며
        count += 1  # 현재 그룹에 해당 모험가를 포함시키기
        if count >= i:  # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
            result += 1 # 총 그룹수 증가
            count = 0 # 현재 그룹에 포함된 모험가의 후 초기화

    print(result)   # 총 그룹의 수 출력
########################  


# testcase_f = ["testcase1.txt", "testcase2.txt"]
testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        line = f.readlines()
        N = int(line[0].strip())   
        group = list(map(int, line[1].split()))

    start_time = time.time()
    
    best_answer(N, group)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)