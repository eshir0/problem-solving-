for T in range(1,int(input())+1):
    N, M, K = map(int,input().split())
    m = [list(map(int,input().split())) for _ in range(N)]

    dir = {}
    for i in range(N):
        for j in range(M):
            if m[i][j] > 0:
                dir[(i,j)] = []
                dir[(i,j)] = [m[i][j],m[i][j]*2]

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    for _ in range(K):

        new_c = {}

        for (y,x), info in dir.items():
            x_p, time = info

            if time == 0:
                continue

            if time == x_p:
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]

                    if (ny,nx) not in dir:

                        if (ny,nx) in new_c:
                            if x_p > new_c[(ny,nx)][0]:
                                new_c[(ny,nx)] = [x_p, x_p * 2]
                        else:
                            new_c[(ny, nx)] = [x_p, x_p * 2]
            dir[(y,x)][1] -= 1

        dir.update(new_c)
    
    ans = 0
    for (y,x), info in dir.items():
        n,k = info
        if k > 0:
            ans += 1

    print(f'#{T} {ans}')