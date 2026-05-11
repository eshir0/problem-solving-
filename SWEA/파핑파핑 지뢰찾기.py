for T in range(1,int(input())+1):
    N = int(input())
    m = [list(input()) for _ in range(N)]

    dy = [0,0,-1,1,-1,1,-1,1]
    dx = [-1,1,0,0,1,1,-1,-1]

    def count(y,x):
        cnt = 0
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == "*":
                cnt += 1
        return cnt
    
    def bfs(sy,sx):
        q = [(sy,sx)]
        m[sy][sx] = '#'

        while q:
            y,x = q.pop(0)

            for i in range(8):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == '.':
                    m[ny][nx] = '#'

                    if count(ny,nx) == 0:
                        q.append((ny,nx))
    
    ans = 0

    for i in range(N):
        for j in range(N):
            if m[i][j] == '.' and count(i,j) == 0:
                ans += 1
                bfs(i,j)
    
    for i in range(N):
        for j in range(N):
            if m[i][j] == '.':
                ans += 1

    print(f'#{T} {ans}')