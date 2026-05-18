from collections import deque
for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input())) for i in range(N)]

    dy = [0,0,1,-1]
    dx = [-1,1,0,0]
    
    v = [[float('inf')] * N for _ in range(N)]
    v[0][0] = 0
    
    q = deque([(0,0,0)])

    while q:
        y,x,c = q.popleft()

        if v[y][x] < c:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                cost = c + m[ny][nx]
                if cost < v[ny][nx]:
                    v[ny][nx] = cost
                    q.append((ny,nx,cost))
    
    print(f'#{T} {v[N-1][N-1]}')