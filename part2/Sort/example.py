# # 선택 정렬
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
    
# print(array)

# # 삽입 정렬 (오름차순)
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     for j in range(i, 0, -1): # start: i, end: 0, step: -1 => range(0,0,-1)일 때는 루프가 안돌아감
#         if array[j] < array[j-1]:  # 왼쪽으로 이동하면서, 순서를 바꿀지 말지 판단하면됨
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break

# print(array)

# # 삽입 정렬 (내림차순)
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     for j in range(i, 0, -1):
#         if array[j] > array[j-1]:
#             array[j-1], array[j] = array[j], array[j-1]
#         else:
#             break
# print(array)

# 퀵 정렬 
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    if start >= end: # 종료 조건
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # left부터 훑는건 pivot보다 큰 것 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # right부터 훑는건 pivot보다 작은 것 찾기
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 엇갈린 경우 (작은 데이터를 피벗 데이터와 교체)
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)
quick_sort(array, 0, len(array)-1)
print(array)