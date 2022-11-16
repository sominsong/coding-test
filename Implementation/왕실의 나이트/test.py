#-------------------------------------------------------#
# 난이도 하 / 풀이 시간 20분 / 시간 제한 2초 / 메모리 제한 128 MB
# 소요 시간: 15분
# Key Idea: 나이트의 8가지 경로를 하나씩 확인하며 각 위치로 이동이 가능한지 확인. 리스트를 이용하여 8가지 방향에 대한 방향 벡터 정의.
#-------------------------------------------------------#

import time
from tracemalloc import start

x = [-1,-1,-2,-2,1,1,2,2]
y = [2,-2,1,-1,2,-2,1,-1]

al_to_int = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}


########################
def answer(pos):
    result = 0
    cur_x = int(al_to_int[pos[0]])
    cur_y = int(pos[1])
    for i in range(8):
        next_x = cur_x + x[i]
        next_y = cur_y + y[i]
        if (next_x >= 1 and next_x <= 8) and (next_y >= 1 and next_y <= 8):
            result += 1
        
    print(result)
########################  

######################## 
# 
def best_answer(pos):
    # 현재 나이트의 위치 입력받기
    row = int(pos[1])
    column = int(ord(pos[0])) - int(ord('a')) + 1 # ord : 문자 -> 아스키 코드 값

    # 나이트가 이동할 수 있는 8가지 방향 정의
    steps = [(-2,-1), (-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]

    # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
    result = 0
    for step in steps:
        # 이동하고자 하는 위치 확인
        next_row = row + step[0]
        next_column = column + step[1]

        # 해당 위치로 이동이 가능하다면 카운트 증가
        if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
            result += 1
    print(result)
#  
########################  


# testcase_f = ["testcase1.txt", "testcase2.txt"]
testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        pos = f.readline().strip()

    start_time = time.time()
    
    answer(pos)
    # best_answer(N)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)