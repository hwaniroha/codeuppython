m = [list(input().split()) for _ in range(10)]

x, y = 1, 1

while 1:
    if m[x][y] == '2':
        m[x][y] = '9'
        break
    m[x][y] = '9'

    if m[x][y + 1] != '1':
        y += 1
    elif m[x + 1][y] != '1':
        x += 1
    else:
        break

for row in m:
    print(' '.join(row))