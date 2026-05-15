for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    num = list(map(int,input().split()))

    ans = -1
    v = [False] * N

    def dfs(n,cost):
        global ans

        if cost > M:
            return

        if n == 2:
            ans = max(ans,cost)
            return

        for i in range(N):
            if not v[i]:
                v[i] = True
                dfs(n+1, cost + num[i])
                v[i] = False

    dfs(0,0)

    print(f'#{T} {ans}')