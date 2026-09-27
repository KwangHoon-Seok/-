# 부품 종류
N = int(input())
item = list(map(int, input().split()))

# 견적서 종류
M = int(input())
estimate = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while True:
        if start < end:
            mid = (start + end) // 2
            if array[mid] == target:
                return mid # 인덱스 번호 반환
            elif array[mid] > target:
                return binary_search(array, target, start, mid - 1)
            else:
                return binary_search(array, target, mid + 1, end)
        else:
            return None

for i in estimate:
    result = binary_search(item, i, 0, N-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
