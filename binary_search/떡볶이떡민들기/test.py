#-------------------------------------------------------#
# 난이도 중 / 풀이 시간 40분 / 시간 제한 2초 / 메모리 제한 128 MB
# 소요 시간: 25분
# 정답 여부: X (최대한 덜 잘랐을 때를 고려 안함, customer == target일 때만 고려)
# Key Idea: 적절한 높이를 찾을 때까지 이진 탐색을 수행하여 높이 H를 반복해서 조정
#           현재 이 높이로 자르면 조건을 만족할 수 있는가를 확인 -> 조건의 만족 여부 (yes or no)에 따라 탐색 범위를 좁혀서 해결
#           0 <= 절단 높이 <= 10억 -> 이렇게 큰 탐색 범위를 볼 경우, 가장 먼저 이진 탐색 떠올려야 함
#-------------------------------------------------------#

import time
from tracemalloc import start
from unittest.case import doModuleCleanups


########################
def binary_search(d, start, end, target):
    if start > end:
        return None
    mid = (start + end)//2
    customer = 0
    for i in d:
        if (i - mid) >= 0:
            customer += (i-mid) 
    if customer == target:
        print(mid)
    elif customer < target:
        binary_search(d, start ,mid-1, target)
    else:
        binary_search(d, mid+1, end, target)

def answer(dduk,n,m):
    max_dduk = max(dduk)
    binary_search(dduk, 0, max_dduk, m)
########################

########################
def better_binary_search(d, start, end, target, result):
    if start > end:
        print(result)
        return
    mid = (start + end)//2
    customer = 0
    for i in d:
        if (i - mid) >= 0:
            customer += (i-mid) 
    if customer == target:
        result = mid
        print(result)
        return
    elif customer < target: # 떡이 적게 잘렸을 경우
        better_binary_search(d, start ,mid-1, target, result)
    else:   # 떡이 많게 잘렸을 경우
        result = mid
        better_binary_search(d, mid+1, end, target, result)

def answer(dduk,n,m):
    max_dduk = max(dduk)
    binary_search(dduk, 0, max_dduk, m)
    result = 0
    better_binary_search(dduk, 0, max_dduk, m, result)
########################


########################
def best_answer(dduk, n, m):
    # 이진 탐색을 위한 시작점과 끝점 설정
    start = 0
    end = max(dduk)

    # 이진 탐색 수행 (반복문)
    result = 0
    while(start <= end):
        total = 0
        mid = (start+end)//2
        for x in dduk:
            # 잘랐을 때의 떡의 양 계산
                if x > mid:
                    total += x - mid
        # 떡의 양이 부족한 경우 더 많이 자르기 (왼쪽 부분 탐색)
        if total < m:
            end = mid -1
        # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
        else:
            result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result 기록
            start = mid + 1
    
    # 정답 출력
    print(result)
########################



testcase_f = ["testcase1.txt", "testcase2.txt"]
# testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        n,m = map(int, f.readline().strip().split())
        dduk = list(map(int, f.readline().strip().split()))

    start_time = time.time()
    
    answer(dduk, n,m)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)