from collections import deque
for T in range(1,11):
    N, start = map(int,input().split())
    m = list(map(int,input().split()))

    node = [[] for _ in range(101)]
    for i in range(0,len(m),2):
        node[m[i]].append(m[i+1])
    
    v = [0] * 101
    v[start] = 1
    q = deque([(start)])

    while q:
        s = q.popleft()
        
        for j in node[s]:
            if v[j] == 0:
                v[j] = v[s] + 1
                q.append(j)
    
    ans = 0
    for i in range(len(v)):
        if max(v) == v[i]:
            ans = max(ans,i)
            
    print(f'#{T} {ans}')