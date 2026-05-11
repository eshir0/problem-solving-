for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    ans = 0
    min_ = 1e9

    li = []

    def bfs(r,c):
        global ans, min_

        q = [(r,c)]
        n = 1

        while q:
            y,x = q.pop(0)

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == m[y][x]+1:
                    n += 1
                    q.append((ny,nx))

        if ans < n:
            ans = n
            min_ = m[r][c]
        elif n == ans:
            if m[r][c] < min_:
                min_ = m[r][c]

    for i in range(N):
        for j in range(N):
            bfs(i,j)

    print(f'#{T} {min_} {ans}')