from collections import deque
for T in range(1,int(input())+1):
    N, M = map(int,input().split())

    m = [[] for i in range(N+1)]
    
    for i in range(M):
        u,v = map(int,input().split())
        m[u].append(v)
        m[v].append(u)
    
    v = [False] * (N+1)
    ans = 0

    for i in range(1, N + 1):
        if not v[i]:
            ans += 1

            q = deque([i])
            v[i] = True

            while q:
                now = q.popleft()

                for nex in m[now]:
                    if not v[nex]:
                        v[nex] = True
                        q.append(nex)
    
    print(f'#{T} {ans}')