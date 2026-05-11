# 직접 혼자푼것
for T in range(1,int(input())+1):
    N = int(input())
    m = [input() for i in range(N)]
    
    cp = [i for i in zip(*m)]

    a = 0
    dy = [0,1,1,1]
    dx = [1,0,1,-1]

    def dfs(r,c,n):
        global a

        q = [(r,c)]
        b = 1

        while q:
            y,x = q.pop(0)
            for i in range(4):
                ny,nx = y,x
                for j in range(4):
                    ny += dy[i]
                    nx += dx[i]
                    if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == 'o':
                        b += 1
                    else:
                        break
                if b >= 5:
                    a += 1
                    break
                b = 1

    for i in range(N):
        for j in range(N):
            if m[i][j] == 'o':
                dfs(i,j,0)
    
    if a >= 1:
        print(f'#{T} YES')
    else:
        print(f'#{T} NO')

# ai가 최적화 한것
for T in range(1, int(input()) + 1):
    N = int(input())
    m = [input() for _ in range(N)]
    
    dy = [0, 1, 1, 1]
    dx = [1, 0, 1, -1]
    
    ans = "NO"
    
    for i in range(N):
        for j in range(N):
            if m[i][j] == 'o':
                for d in range(4):
                    ny, nx = i, j
                    cnt = 1
                    
                    # 해당 방향으로 4칸 더 직진
                    for _ in range(4):
                        ny += dy[d]
                        nx += dx[d]
                        if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == 'o':
                            cnt += 1
                        else:
                            break
                    
                    if cnt == 5:
                        ans = "YES"
                        break
            if ans == "YES":
                break
        if ans == "YES":
            break
            
    print(f'#{T} {ans}')