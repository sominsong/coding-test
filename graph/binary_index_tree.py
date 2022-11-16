### Bianry Index Tree (BIT, Fenwick Tree) ###
# 조건: 데이터 update가 빈번한 상황에서 interval sum (구간 합) 문제
# 원리: 2진법 인덱스를 활용 -> 0이 아닌 비트 = 내가 저장하고 있는 값의 범위(개수) 의미

# 데이터 개수(n), 구간 합 횟수(m), 데이터 변경 횟수(k)
n,m,k = 12, 2, 1

# input data
    #  0  1  2  3  4  5  6  7  8  9  10 11 12
arr = [0, 2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
# bianry index tree
tree = [0] * (n+1)
# input (operation(0:interval sum, 1:update), ...)
# interval sum의 경우: (0, start, end)
# update의 경우: (1, index, value)
input = [(0,2,6),(1,3,5),(0,2,6)]

# i번째 수까지의 누적 합을 계산하는 함수
def prefix_sum(i):
    sum = 0
    while i > 0:
        sum += tree[i]
        # index를 i&-i만큼 뺴가면서 이동
        i -= (i & -i)
    return sum

# i번째 수를 dif 값만큼 update하는 함수
def update(i, dif):
    while i <= n:
        tree[i] += dif
        # index를 i&-i만큼 더하면서 이동
        i += (i & -i)

# start에서 end 사이의 합을 계산하는 함수
def interval_sum(start, end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1, n+1):
    # binary index tree 초기화
    update(i, arr[i])

for i in range(m+k):
    # operation, a, b
    op, a, b = input[i]
    if op == 0: # interval sum
        print(interval_sum(a, b))
    else: # update
        update(a, b-arr[a])    # b-arr[i] = dif
        arr[i] = b

    



