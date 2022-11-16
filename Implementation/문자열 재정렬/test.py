#-------------------------------------------------------#
# 난이도 하 / 풀이 시간 20분 / 시간 제한 1초 / 메모리 제한 128 MB
# 소요 시간: 6분
# Key Idea: 문자를 하나씩 확인 -> 숫자인 경우 따로 합계 계산, 알파벳은 별도의 리스트에 저장 -> 결과적으로 리스트 저장된 알파벳 정렬, 합계를 뒤에 붙여 출력
#-------------------------------------------------------#

import time
from tracemalloc import start
from unittest import result


########################
def answer(input):
    result = []
    int_sum = 0
    for i in input:
        if i.isalpha():
            result.append(i)
        else:
            int_sum += int(i)
    result.sort()
    result.append(str(int_sum))

    print("".join(result))
########################

########################
def best_answer(input):
    result = []
    value = 0

    # 문자를 하나씩 확인하며
    for x in input:
        # 알파벳인 경우 결과 리스트 삽입
        if x.isalpha():
            result.append(x)
        # 숫자는 따로 더하기
        else:
            value += int(x)
    # 알파벳을 오름차순으로 정렬
    result.sort()
    # 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
    if value != 0:
        result.append(str(value))
    # 최종 결과 출력(리스트를 문자열로 변환하여 출력)
    print("".join(result))
########################


testcase_f = ["testcase1.txt", "testcase2.txt"]
# testcase_f = ["testcase1.txt"]
for testcase in testcase_f:
    with open(testcase, "r") as f:
        input = f.readline().strip()

    start_time = time.time()
    
    answer(input)
    
    end_time = time.time()
    print(testcase, " - time: ", end_time - start_time)