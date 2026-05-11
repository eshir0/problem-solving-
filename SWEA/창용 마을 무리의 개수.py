for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    
    dir ={i: [] for i in range(1, N+1)}

    for _ in range(M):
        u, v = map(int,input().split())
        dir[u].append(v)
        dir[v].append(u)

    v = set()
    ans = 0

    for i in range(1, N + 1):
        if i not in v:
            ans += 1

            q = [i]
            v.add(i)

            while q:
                c = q.pop(0)
                for net in dir[c]:
                    if net not in v:
                        v.add(net)
                        q.append(net)
                        
    print(f'#{T} {ans}')