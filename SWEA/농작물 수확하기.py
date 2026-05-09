from collections import deque
for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input())) for _ in range(N)]

    ans = 0
    mid = N // 2
    
    for i in range(N):
        d = abs(mid - i)

        for j in range(d,N-d):
            ans += m[i][j]

    print(f'#{T} {ans}')