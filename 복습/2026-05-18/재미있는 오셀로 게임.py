# 1 : 흑돌, 2 : 백돌
for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    m = [[0] * N for i in range(N)]

    mid = N//2
    m[mid][mid-1] = 1
    m[mid][mid] = 2
    m[mid-1][mid] = 1
    m[mid-1][mid-1] = 2

    dy = [0,0,-1,1,-1,1,-1,1]
    dx = [-1,1,0,0,1,1,-1,-1]
    
    r = {1: 2, 2: 1}

    for _ in range(M):
        x, y, ck = map(int,input().split())
        x -= 1
        y -= 1
        m[y][x] = ck

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == r[ck]:
                ny,nx = y,x
                a = 0
                for j in range(N*2):
                    ny += dy[i]
                    nx += dx[i]
                    if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == 0:
                        a = 0
                        break
                    elif 0 <= ny < N and 0 <= nx < N and m[ny][nx] == ck:
                        a += 1
                        break

                ny,nx = y,x
                if a == 1:
                    for j in range(N*2):
                        ny += dy[i]
                        nx += dx[i]
                        if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == r[ck]:
                            m[ny][nx] = ck
                        elif 0 <= ny < N and 0 <= nx < N and m[ny][nx] == ck:
                            break

    w,b = 0,0
    for i in m:
        for j in i:
            if j == 1:
                b += 1
            elif j == 2:
                w += 1
    print(f'#{T} {b} {w}')