for T in range(1,int(input())+1):
    N, M = map(int,input().split())

    node = [[] for _ in range(N+1)]
    for _ in range(M):
        u,v = map(int,input().split())
        node[u].append(v)
        node[v].append(u)

    v = [False] * (N + 1)
    ans = 1

    def dfs(now, cnt):
        global ans
        ans = max(ans,cnt)

        for i in node[now]:
            if not v[i]:
                v[i] = True
                dfs(i, cnt + 1)
                v[i] = False
    
    for i in range(1, N + 1):
        v[i] = True
        dfs(i, 1)
        v[i] = False

    print(f'#{T} {ans}')