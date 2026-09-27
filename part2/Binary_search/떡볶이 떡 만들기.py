# N: 떡의 개수, M: 요청한 떡의 길이
N, M = map(int, input().split())
# 각각의 떡 길이
array = list(map(int, input().split()))

# 종료 조건 필요
def binary_search(array, target, start, end):
    if start < end:
        mid = (start + end) // 2
        sum = 0 
        for i in array:
            temp = i - mid
            if temp >= 0:
                sum += temp
        if sum == target:
            return mid
        elif sum < target:
            return binary_search(array, target, start, mid - 1)
        elif sum > target:
            return binary_search(array, target, mid + 1, end)
    else:
        return None

start = 0
end = max(array)

result = binary_search(array, M, start, end)

print(result)