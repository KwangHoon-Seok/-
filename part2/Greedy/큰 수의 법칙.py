N , M, K = map(int, input().split()) # M번 더하되, 같은 수는 K번 까지만 반복 (중복 허용)
data = list(map(int, input().split())) # N개 데이터 넣고 

first_max = max(data)
data.remove(first_max)
second_max = max(data)
count = 0
result = 0 
for i in range(M):
    if (count < K):
        result += first_max
        count += 1
    elif count == K:
        result += second_max
        count = 0
print(result)


