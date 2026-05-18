for T in range(1,int(input())+1):
    N, B = map(int,input().split())
    H = list(map(int,input().split()))

    ans = 1e9
    def dfs(n,cost):
        global ans

        if ans < cost - B:
            return

        if n == N:
            if cost >= B:
                a = cost - B
                ans = min(ans,a)
            return
        
        dfs(n+1,cost+H[n])
        dfs(n+1,cost)
    
    dfs(0,0)
    print(f'#{T} {ans}')