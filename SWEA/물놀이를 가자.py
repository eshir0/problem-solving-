from collections import deque

for T in range(1,int(input())+1):
    N,M = map(int,input().split())
    m = [input() for i in range(N)]

    Map = [[-1] * M for i in range(N)]

    q = deque()

    for i in range(N):
        for j in range(M):
            if m[i][j] == "W":
                q.append((i,j))
                Map[i][j] = 0

    ans = 0

    while q:
        y,x = q.popleft()

        for dy,dx in ((-1,0), (1,0), (0,-1), (0,1)):
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M and Map[ny][nx] == -1:
                Map[ny][nx] = Map[y][x] + 1
                ans += Map[ny][nx]
                q.append((ny,nx))

    print(f'#{T} {ans}')