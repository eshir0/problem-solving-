# 직접 푼 버전
for T in range(1,int(input())+1):
    H,W = map(int,input().split())
    m = [list(input()) for _ in range(H)]
    N = int(input())
    num = input()

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    dir = {'U': 2,'D' : 3,'L' : 0, 'R' : 1}

    def dfs(y,x,d,n):
        
        if n == N:
            return

        ny, nx = y,x
        
        if num[n] == "U":
            ny += dy[dir["U"]]
            nx += dx[dir["U"]]
            if 0 <= ny < H and 0 <= nx < W and m[ny][nx] == ".":
                m[ny][nx] = "^"
                m[y][x] = "."
                dfs(ny,nx,dir["U"],n+1)
                return
            m[y][x] = "^"
            dfs(y,x,dir["U"],n+1)
            return

        elif num[n] == "D":
            ny += dy[dir["D"]]
            nx += dx[dir["D"]]
            if 0 <= ny < H and 0 <= nx < W and m[ny][nx] == ".":
                m[ny][nx] = "v"
                m[y][x] = "."
                dfs(ny,nx,dir["D"],n+1)
                return
            m[y][x] = "v"
            dfs(y,x,dir["D"],n+1)
            return

        elif num[n] == "L":
            ny += dy[dir["L"]]
            nx += dx[dir["L"]]
            if 0 <= ny < H and 0 <= nx < W and m[ny][nx] == ".":
                m[ny][nx] = "<"
                m[y][x] = "."
                dfs(ny,nx,dir["L"],n+1)
                return
            m[y][x] = "<"
            dfs(y,x,dir["L"],n+1)
            return
        
        elif num[n] == "R":
            ny += dy[dir["R"]]
            nx += dx[dir["R"]]
            if 0 <= ny < H and 0 <= nx < W and m[ny][nx] == ".":
                m[ny][nx] = ">"
                m[y][x] = "."
                dfs(ny,nx,dir["R"],n+1)
                return
            m[y][x] = ">"
            dfs(y,x,dir["R"],n+1)
            return
        
        elif num[n] == "S":
            while True:
                ny += dy[d]
                nx += dx[d]
                if 0 <= ny < H and 0 <= nx < W:
                    if m[ny][nx] == "*":
                        m[ny][nx] = "."
                        dfs(y,x,d,n+1)
                        return
                    elif m[ny][nx] == "#":
                        break
                else:
                    break
            dfs(y,x,d,n+1)
            return
    
    a = 0
    for i in range(H):
        for j in range(W):
            if m[i][j] == "v":
                dfs(i,j,3,0)
                a = 1
                break
            elif m[i][j] == ">":
                dfs(i,j,1,0)
                a = 1
                break
            elif m[i][j] == "<":
                dfs(i,j,0,0)
                a = 1
                break
            elif m[i][j] == "^":
                dfs(i,j,2,0)
                a = 1
                break   
        if a == 1:
            break
    
    print(f'#{T}',end=' ')
    for i in range(H):
        print(''.join(m[i]))

# ai 버전
for T in range(1, int(input()) + 1):
    H, W = map(int, input().split())
    m = [list(input()) for _ in range(H)]
    N = int(input())
    commands = input()

    dy = [0, 0, -1, 1]  # 좌(0), 우(1), 상(2), 하(3)
    dx = [-1, 1, 0, 0]
    
    # 방향 매핑 (회원님 코드의 로직 활용)
    dir_idx = {'L': 0, 'R': 1, 'U': 2, 'D': 3}
    dir_shape = {0: '<', 1: '>', 2: '^', 3: 'v'}

    # 1. 초기 전차 위치 및 방향 찾기
    cy, cx, cd = 0, 0, 0
    for i in range(H):
        for j in range(W):
            if m[i][j] in ['^', 'v', '<', '>']:
                cy, cx = i, j
                if m[i][j] == '<': cd = 0
                elif m[i][j] == '>': cd = 1
                elif m[i][j] == '^': cd = 2
                elif m[i][j] == 'v': cd = 3
                break

    # 2. 명령어 순차 실행 (dfs 대신 for문 사용)
    for cmd in commands:
        if cmd in ['U', 'D', 'L', 'R']:
            # 2-1. 먼저 전차 방향을 돌림
            cd = dir_idx[cmd]
            m[cy][cx] = dir_shape[cd]
            
            # 2-2. 바라보는 방향의 앞칸 확인
            ny = cy + dy[cd]
            nx = cx + dx[cd]
            
            # 2-3. 평지면 이동
            if 0 <= ny < H and 0 <= nx < W and m[ny][nx] == '.':
                m[cy][cx] = '.'          # 원래 있던 곳은 평지로
                cy, cx = ny, nx          # 좌표 이동
                m[cy][cx] = dir_shape[cd] # 새 위치에 전차 배치

        elif cmd == 'S':
            # 포탄 발사 로직 (회원님 코드와 동일)
            ny, nx = cy, cx
            while True:
                ny += dy[cd]
                nx += dx[cd]
                if 0 <= ny < H and 0 <= nx < W:
                    if m[ny][nx] == '*':    # 벽돌 벽 파괴
                        m[ny][nx] = '.'
                        break
                    elif m[ny][nx] == '#':  # 강철 벽에 막힘
                        break
                else:
                    break # 맵 밖으로 벗어남

    # 3. 결과 출력
    print(f'#{T}', end=' ')
    for row in m:
        print(''.join(row))