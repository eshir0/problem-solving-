from collections import deque
for T in range(1,int(input())+1):
    N,W,H = map(int,input().split())
    m = [list(map(int,input().split())) for _ in range(H)]

    p = []

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    ans = 1e9

    def dfs(level):
        global ans

        if level == N:
            cp = [row[:] for row in m]
            
            # 찾은 구슬 위치를 통한 시작
            for col in p:
                for i in range(H):
                    if cp[i][col] > 0:
                        
                        q = deque([(i, col, cp[i][col])])
                        cp[i][col] = 0

                        # 벽돌 연쇄반응 코드
                        while q:
                            y,x,power = q.popleft()
                            if power == 1:
                                continue

                            for d in range(4):
                                for k in range(1,power):
                                    ny = y + dy[d] * k
                                    nx = x + dx[d] * k

                                    if 0 <= ny < H and 0 <= nx < W and cp[ny][nx] > 0:
                                        q.append((ny,nx,cp[ny][nx]))
                                        cp[ny][nx] = 0
                        break
                
                # 남아있는 벽돌 떨어지는 중력 코드
                for c in range(W):
                    z = []
                    for r in range(H):
                        if cp[r][c] > 0:
                            z.append(cp[r][c])
                            cp[r][c] = 0

                    row_idx = H -1
                    while z:
                        cp[row_idx][c] = z.pop()
                        row_idx -= 1

            # 남아있는 벽돌 세기 (답 갱신)
            b = 0
            for i in range(H):
                for j in range(W):
                    if cp[i][j] > 0:
                        b += 1
            ans = min(ans,b)       
            return
        
        # 떨어트릴 모든 구슬들의 위치
        for i in range(W):
            p.append(i)
            dfs(level + 1)
            p.pop()
    dfs(0)

    print(f'#{T} {ans}')

# 좀 다른 방식
from collections import deque
for T in range(1,int(input())+1):
    N,W,H = map(int,input().split())
    m = [list(map(int,input().split())) for i in range(H)]

    ans = 1e9

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    def dfs(n,cp):
        global ans

        if n == N:
            a = 0
            for i in range(H):
                for j in range(W):
                    if cp[i][j] > 0:
                        a += 1
            ans = min(ans,a)
            return

        for i in range(W):
            cp_m = [row[:] for row in cp]

            for j in range(H):
                if cp_m[j][i] > 0:
                    q = deque([(j,i,cp_m[j][i])])
                    cp_m[j][i] = 0

                    while q:
                        y,x,k = q.popleft()
                        for d in range(4):
                            ny,nx = y,x

                            for _ in range(k-1):
                                ny += dy[d]
                                nx += dx[d]
                                if 0 <= ny < H and 0 <= nx < W:
                                    if cp_m[ny][nx] > 0:
                                        q.append((ny,nx,cp_m[ny][nx]))
                                    cp_m[ny][nx] = 0
                    break
            for c in range(W):
                tem = []

                for r in range(H):
                    if cp_m[r][c] > 0:
                        tem.append(cp_m[r][c])
                        cp_m[r][c] = 0

                for r in range(H -1 , -1 , -1):
                    if tem:
                        cp_m[r][c] =  tem.pop()
                    else:
                        break
            dfs(n + 1, cp_m)

    dfs(0,m)
    print(f'#{T} {ans}')