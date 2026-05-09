for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    m = [list(map(int,input().split())) for _ in range(N)]

    ans = 0

    def dfs(y,x):
        global ans

        a = 0
        for i in range(y,y+M):
            for j in range(x,x+M):
                a += m[i][j]
        ans = max(ans,a)

    for i in range(N-M+1):
        for j in range(N-M+1):
            dfs(i,j)
    print(f'#{T} {ans}')