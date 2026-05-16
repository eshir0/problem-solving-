for T in range(1,int(input())+1):
    N, K = map(int,input().split())
    A = list(map(int,input().split()))

    ans = 0

    def dfs(n,cost):
        global ans
        
        if cost > K:
            return

        if n == N:
            if cost == K:
                ans += 1
            return

        dfs(n+1, cost + A[n])
        dfs(n+1, cost)

    dfs(0,0)
    print(f'#{T} {ans}')