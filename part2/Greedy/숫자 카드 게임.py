# 숫자가 쓰인 카드들이 N * M 형태로
# 먼저 뽑고자 하는 카드가 포함되어 있는 행 선택
# 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 함
# 처음에 카드를 골라낼 행을 선택할 때, 해당 행에서 가장 숫자가 낮은 카드를 뽑는 것을 고려하여
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 해야 함

N, M = map(int, input().split())

cards = [] 

for i in range(N):
    data = list(map(int, input().split()))
    cards.append(data)

values = []
for i in range(N):
    values.append(min(cards[i]))

print(max(values))