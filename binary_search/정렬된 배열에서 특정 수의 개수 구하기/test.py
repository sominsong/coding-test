#-------------------------------------------------------#
# 난이도 중 / 풀이 시간 30분 / 시간 제한 1초 / 메모리 제한 128 MB
# 소요 시간: 5분
# 정답 여부: X (배열에 없는 경우 틀렸음)
# Key Idea: O(logN) 시간 복잡도 -> 데이터가 정렬되어 있기 때문에 이진 탐색 수행 가능
#           특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 위치 차이를 계산해 문제 해결 가능
#-------------------------------------------------------#

from re import L
import time
from tracemalloc import start


########################
from bisect import bisect_left, bisect_right
def answer(array, n,x):
    left = bisect_left(array, x)
    if left == 0 or left == n:  ## 배열에 없음
        print(-1)
    else:
        right = bisect_right(array, x)    
        print(right - left)
########################


########################
def better_answer(array, n, x):
    left=bisect_left(array, x)
    right=bisect_right(array, x)
    if right - left == 0:   # 배열에 없음
        print(-1)
    else:
        print(right-left)
########################


########################
def best_answer(array, n, x):
    # 값이 [x,x] 범위에 있는 데이터의 개수 계산
    right_index = bisect_right(array, x)
    left_index = bisect_left(array, x)
    count = right_index - left_index

    # 값이 x인 원소가 존재하지 않는다면
    if count == 0:
        print(-1)
    # 값이 x인 원소가 존재한다면
    else:
        print(count)
########################


# testcase_f = ["testcase1.txt", "testcase2.txt"]
testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        n,x = map(int, f.readline().strip().split())
        array = list(map(int, f.readline().strip().split()))

    start_time = time.time()
    
    answer(array, n,x)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)