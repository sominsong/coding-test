#-------------------------------------------------------#
# 난이도 하 / 풀이 시간 15분 / 시간 제한 2초 / 메모리 제한 128 MB
# 소요 시간: 5분
# Key Idea: 두 수 중에서 하나라도 0 혹은 1인 경우, 곱하기보다는 더하기를 수행하는 것이 효율적
#-------------------------------------------------------#

import time
from tracemalloc import start

########################
def answer(n):
    result = int(n[0])
    n_len = len(n)
    for i in range(1,n_len):
        if result * int(n[i]) == 0 or result * int(n[i]) == result:
            result += int(n[i])
        else:
            result *= int(n[i])
    print(result)
########################

########################
def best_answer(n):
    result = int(n[0])

    for i in range(1, len(result)):
        # 두 수 중에서 하나라도 '0'혹은 '1'인 경우, 곱하기 보다는 더하기 수행
            num = int(n[i])
            if num <= 1 or result <= 1:
                rsult += num
            else:
                result *= num
    print(result)
########################


testcase_f = ["testcase1.txt", "testcase2.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        N = f.readline().strip()

    start_time = time.time()
    
    answer(N)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)