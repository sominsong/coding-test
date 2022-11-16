#-------------------------------------------------------#
# 난이도 하 / 풀이 시간 30분 / 시간 제한 1초 / 메모리 제한 128 MB
# 소요 시간: 분
# 정답 여부: 
# Key Idea: 
#-------------------------------------------------------#

import time
from tracemalloc import start


########################

########################


# testcase_f = ["testcase1.txt", "testcase2.txt"]
testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        line = f.readline().strip()

    start_time = time.time()
    
    # answer()
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)