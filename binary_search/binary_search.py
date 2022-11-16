### recursive ###
def binary_search_rec(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    # mid == target
    if array[mid] == target:
        return mid
    # target < mid
    elif array[mid] > target:
        return binary_search_rec(array, target, start, mid-1)
    # mid < target
    elif array[mid] < target:
        return binary_search_rec(array, target, mid+1, end)

n, target = 10, 7
array = [1,3,5,7,9,11,13,15,17,19]

result = binary_search_rec(array, target, 0, n-1)
print(array, " target: ", target)
if result == None: 
    print("There is not " + target)
else:
    print(result + 1)


### Iteration ###
def binary_search_iter(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        # mid == target
        if array[mid] == target:
            return mid
        # mid > target
        elif target < array[mid]:
            end = mid-1
        # mid < target
        else:
            start = mid+1
    return None

n, target = 10, 7
array = [1,3,5,7,9,11,13,15,17,19]

result = binary_search_iter(array, target, 0, n-1)
print(array, " target: ", target)
if result == None: 
    print("There is not " + target)
else:
    print(result + 1)