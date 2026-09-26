# Iterable 자료형

### List 자료형

a = [ ] , 리스트의 원소를 수정 혹은 할당하려면 초기화가 필수적임

1차원 리스트 초기화 : a = [0]*n , a = [ i for i in range(20) if i % 2 == 1 ]

2차원 리스트[m,n] 초기화: a = [ [0] * n for _ in range(m) ]

리스트 관련 기타 메서드

* append() -> O(1)
* sort(), sort(reverse = True) -> O(NlogN)

* reverse() -> O(N)
* insert(index, value) -> O(N)

* count(value) -> O(N)
* remove(value) -> O(N)

### 문자열 자료형

### 튜블 자료형

리스트와 비슷하지만 한 번 선언한 값을 변경할 수 없음

불변 속성 때문에 dict의 key로 사용하거나, heapq의 원소로 사용가능

# non-iterable 자료형

### 사전 자료형

key와 value 쌍으로 이루어져 있음

a = dict(), a[key] = value

### 집합 자료형

집합은 기본적으로 리스트 혹은 문자열을 이용하여 만들 수 있음.

* 중복 허용 x
* 순서 x

a = set([1,2,3,3,4])

* 합집합 a | b
* 교집합 a & b
* 차집합 a - b

# 주요 라이브러리

### itertools

1. permutations(순열) -> iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우 계산
2. combinations(조합) -> iterable 객체에서 r개의 데이터로를 뽑아 순서를 고려하지 않고 모든 경우 계산
3. product -> permutations 달리 r개의 데이터를 뽑을 때 중복을 허용함
4. combinations_with_replacement -> combinations과 달리 r개의 데이터를 뽑을 때 중복을 허용

### heapq

heap 기능을 사용하기 위해 사용되는 라이브러리

1. 원소 삽입: heapq.heappush()
2. 원소 추출: headq.heappop()

해당 라이브러리는 max heap을 제공하지 않으므로 max heap을 구현하려면 값의 부호를 반전 시켜서 구현해야함

### bisect

이진 탐색을 구현할 수 있도록 하는 라이브러리

1. bisect_left(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾음
2. bisect_right(a, x): 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾음

### collections

1. deque를 사용하여 queue 자료 구조 구현. 원소 삽입: append(), 원소 삭제: popleft()
2. Counter 등장 횟수를 세는 기능
