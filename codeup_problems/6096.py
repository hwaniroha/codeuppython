h, w = input().split()
h = int(h)
w = int(w)

grid = [[0] * w for _ in range(h)]

n = int(input())

for _ in range(n):
    l, d, x, y = input().split()
    l = int(l)
    d = int(d)
    x = int(x) - 1
    y = int(y) - 1

    if d == 0:
        for i in range(l):
            grid[x][y + i] = 1
    else:
        for i in range(l):
            grid[x + i][y] = 1

for row in grid:
    print(' '.join(str(cell) for cell in row))