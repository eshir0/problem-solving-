for T in range(1,11):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    m = [i for i in zip(*m)]

    ans = 0

    for i in range(N):
        v = False

        for j in range(N):
            if m[i][j] == 1:
                v = True
            
            elif m[i][j] == 2:
                if v:
                    ans += 1
                    v = False

    print(f'#{T} {ans}')