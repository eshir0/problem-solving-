from collections import deque
for T in range(1,11):
    n = int(input())
    m = [list(map(int,input().split())) for i in range(100)]


    start = deque()
    for i in range(100):
        if m[99][i] == 2:
            start.append((99,i))
            break

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    while start:
        y,x = start.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 100 and 0 <= nx < 100 and m[ny][nx] == 1:
                m[ny][nx] = 2
                start.append((ny,nx))
                break

    X = 0
    for i in range(100):
        if m[0][i] == 2:
            X = i

    print(f'#{T} {X}')