N = str(input())
row, col = ord(N[0]) - ord('a') + 1, int(N[1])
# x = row, y = col
type = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

result = 0

for move in type: 
    x = row + move[0]
    y = col + move[1]
    if 1 <= x <= 8 and 1 <= y <= 8:
        result += 1

print(result)


# a의 아스키 수는 97이며, 아스키 코드를 구할 때는 ord() 함수를 사용한다.