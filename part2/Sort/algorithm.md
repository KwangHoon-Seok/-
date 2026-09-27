## 선택 정렬

"가장 작은 것을 선택" 하여 앞으로 보내는 과정 (오름차순 기준)

```
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     min_index = i
#     for j in range(i+1, len(array)):
#         if array[min_index] > array[j]:
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]
  
# print(array)
```

## 삽입 정렬

"데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입하면 어떨까?"

현재 선택된 원소의 이전 원소들과 각각 비교해보며, 자리를 바꿀지 말지 결정한다.

```

# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(array)):
#     for j in range(i, 0, -1): # start: i, end: 0, step: -1 => range(0,0,-1)일 때는 루프가 안돌아감
#         if array[j] < array[j-1]:  # 왼쪽으로 이동하면서, 순서를 바꿀지 말지 판단하면됨
#             array[j], array[j-1] = array[j-1], array[j]
#         else:
#             break

# print(array)
```

## 퀵 정렬

"기준 데이터를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸면 어떨까?"
