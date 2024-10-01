board = [list(input().split()) for _ in range(19)]
n = int(input())

for _ in range(n):
    x, y = input().split()
    x = int(x) - 1
    y = int(y) - 1

    for i in range(19):
        if i != y:
            board[x][i] = '1' if board[x][i] == '0' else '0'

    for i in range(19):
        if i != x:
            board[i][y] = '1' if board[i][y] == '0' else '0'

for row in board:
    print(' '.join(row))