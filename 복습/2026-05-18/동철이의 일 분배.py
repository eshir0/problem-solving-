for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    v = [False] * N
    ans = float(-1e9)

    def dfs(n,cost):
        global ans

        if cost <= ans:
            return

        if n == N:
            ans = max(ans,cost)
            return

        for i in range(N):
            if not v[i]:
                v[i] = True
                dfs(n+1,cost * (m[n][i] * 0.01))
                v[i] = False

    for i in range(N):
        v[i] = True
        dfs(1,m[0][i])
        v[i] = False

    print(f'#{T} {ans:.6f}')