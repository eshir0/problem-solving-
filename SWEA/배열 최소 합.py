for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    v = [False] * N
    ans = 1e9

    def dfs(n,cost):
        global ans  

        if cost > ans:
            return
              
        if n == N:
            ans = min(ans,cost)
            return
        
        for i in range(N):
            if not v[i]:
                v[i] = True
                dfs(n+1,cost + m[n][i])
                v[i] = False

    dfs(0,0)
    print(f'#{T} {ans}')