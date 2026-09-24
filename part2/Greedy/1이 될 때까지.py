# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다. 
N, K = map(int, input().split())

count = 0
while (True):
    if (N % K) == 0:
        N //= K
        count += 1
    elif N == 1:
        print(count)
        break
    else:
        N -= 1
        count += 1


