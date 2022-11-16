### 피보나치 - Top-Down ###

# DP Table 선언
cache = [0] * 100

# 피보나치 함수 재귀 선언
def fibo(x):
    if x == 1 or x == 2:    # 첫번째 or 두번째면
        return 1
    if cache[x] != 0:   # caching되어 있다면
        return cache[x]
    # 한 번도 수행하지 않았다면 재귀 호출
    cache[x] = fibo(x-1) + fibo(x-2)

    return cache[x]

print(fibo(99))


### 피보나치 - Botto-Up ###

# DP Table 선언
d = [0] * 100

# 첫 번째, 두 번째 피보나치 수는 1로 초기화
d[1] = 1
d[2] = 1
n = 99

# 반복문으로 피보나치 함수
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])