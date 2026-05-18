for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input())) for i in range(N)]

    mid = N//2

    ans = 0

    for i in range(N):
        for j in range(N):
            if abs(mid - i) + abs(mid - j) <= mid:
                ans += m[i][j]

    print(f'#{T} {ans}')