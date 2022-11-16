import time
from tracemalloc import start

### selection sort ###

array = [7,5,9,0,3,1,6,2,4,8]

start_time = time.time()
for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[min_index], array[i] = array[i], array[min_index]
end_time = time.time()
print("Selection Sort", " - time: ", end_time - start_time)
print(array)


### Insertion Sort ###

array = [7,5,9,0,3,1,6,2,4,8]

start_time = time.time()
for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
end_time = time.time()
print("Insertion Sort", " - time: ", end_time - start_time)
print(array)


### Quick Sort ###

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    # 원소가 한 개인 경우 종료
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end
    while(left <= right):
        # left = pivot보다 큰 수
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # right = pivot보다 작은 수
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        # left right 역전 된 경우
        if left > right:
            # pivot이랑 right랑 자리 바꿈
            array[pivot], array[right] = array[right], array[pivot]
        else:
            # left랑 right랑 자리 바꿈
            array[left], array[right] = array[right], array[left]
    # 원래 pivot의 왼쪽, 오른쪽도 똑같이 quick sort
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

start_time = time.time()
quick_sort(array, 0, len(array)-1)
end_time = time.time()
print("Quick Sort", " - time: ", end_time - start_time)
print(array)


### Quick Sort (python ver) ###

array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

start_time = time.time()
array = quick_sort(array)
end_time = time.time()
print("Quick Sort", " - time: ", end_time - start_time)
print(array)


### Counting Sort ###

array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

count = [0] * (max(array)+1)

for i in array:
    count[i] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")
