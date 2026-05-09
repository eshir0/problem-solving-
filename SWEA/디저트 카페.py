for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for _ in range(N)]

    ans = -1
    v = []

    dy = [1,1,-1,-1]
    dx = [1,-1,-1,1]

    def dfs(y,x, d, sy,sx):
        global ans

        for nd in (d,d+1):
            if  nd <= 3:
                ny = y + dy[nd]
                nx = x + dx[nd]

                if ny == sy and nx == sx:
                    ans = max(ans, len(v))
                    return
                
                if 0 <= ny < N and 0 <= nx < N and m[ny][nx] not in v:
                    v.append(m[ny][nx])
                    dfs(ny,nx,nd,sy,sx)
                    v.pop()

    for i in range(N):
        for j in range(N):
            v.append(m[i][j])
            dfs(i,j,0,i,j)
            v.pop()
    
    print(f'#{T} {ans}')