for T in range(1,int(input())+1):
    N, L = map(int,input().split())
    K = [list(map(int,input().split())) for i in range(N)]

    v = [False] * N

    ans = 0
    def dfs(n,cost,u):
        global ans

        if cost > L:
            return
        
        if u > ans:
            ans = max(ans,u)
        

        for i in range(n,N):
            u = u + K[i][0]
            dfs(i+1, cost + K[i][1], u)
            u = u - K[i][0]
    
    dfs(0,0,0)
    print(f'#{T} {ans}')