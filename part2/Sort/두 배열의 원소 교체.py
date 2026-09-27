N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B, reverse=True)
count = 0
i = 0
while True:
    if count == K:
        break
    if A[i] != B[i]:
        A[i], B[i] = B[i], A[i]
        count += 1
        i += 1
    else:
        i += 1
    

print(sum(A))
