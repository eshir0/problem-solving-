for T in range(1,int(input())+1):
    N = int(input())
    m = [[0] * N for _ in range(N)]

    dy = [0,1,0,-1]
    dx = [1,0,-1,0]

    q = [(0,0)]
    m[0][0] = 1
    c = 1

    for i in range(N**2):
        y,x = q.pop(0)
        ny,nx = y,x
        for j in range(N-1):
            ny += dy[i%4]
            nx += dx[i%4]
            if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == 0:
                m[ny][nx] = c + 1
                c += 1
            else:
                break
        q.append((ny,nx))
            
    print(f'#{T}')
    for i in range(N):
        print(*m[i])