#-------------------------------------------------------#
# 난이도 하 / 풀이 시간 15분 / 시간 제한 2초 / 메모리 제한 128 MB
# 소요 시간: 11분
# 정답 여부: X
# Key Idea: 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체 -> A는 오름차순, B는 내림차순 정렬 -> 이후 A의 원소가 B의 원소보다 작을 때에만 교체를 수행
#-------------------------------------------------------#

import time
from tracemalloc import start


########################
# counting sort 사용 -> N개로 한정되어 있으면서, 반복이 많기 때문
def answer(a,b,n,k):
    count_a = [0] * (max(a)+1)
    count_b = [0] * (max(b)+1)

    for i in a:
        count_a[i] += 1
    for j in b:
        count_b[j] += 1

    sorted_a, sorted_b = [], []

    for i in range(len(count_a)):
        if count_a[i]:
            for _ in range(count_a[i]):
                sorted_a.append(i)
    for i in range(len(count_b)-1,0,-1):
        if count_b[i]:
            for _ in range(count_b[i]):
                sorted_b.append(i)

    for i in range(k):
        sorted_a[i], sorted_b[i] = sorted_b[i], sorted_a[i]

    result = 0
    for x in sorted_a:
        result += x
    
    print(result)
########################

########################
# 파이썬의 sort 라이브러리 이용
def best_answer(a,b,n,k):
    a.sort() # 오름차순 정렬
    b.sort(reverse=True) # 내림차순 정렬

    # 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
    for i in range(k):
        # A의 원소가 B의 원소보다 작은 경우
        if a[i] < b[i]:
            # 두 원소를 교체
            a[i], b[i] = b[i], a[i]
        else:
            break
    print(sum(a)) # 배열 A의 모든 원소의 합 출력
########################


# testcase_f = ["testcase1.txt", "testcase2.txt"]
testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        n,k = map(int, f.readline().strip().split())
        a = list(map(int, f.readline().strip().split()))
        b = list(map(int, f.readline().strip().split()))

    start_time = time.time()
    
    # answer(a,b,n,k)
    best_answer(a,b,n,k)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)