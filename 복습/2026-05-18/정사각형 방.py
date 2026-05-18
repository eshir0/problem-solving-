from collections import deque
for T in range(1,int(input())+1):
    N = int(input())
    m = [list(map(int,input().split())) for i in range(N)]

    dy = [0,0,-1,1]
    dx = [-1,1,0,0]

    ans = []
    def bfs(sy,sx):
        global ans

        q = deque([(sy,sx)])
        cnt = 1

        while q:
            y,x = q.popleft()

            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == m[y][x] + 1:
                    cnt += 1
                    q.append((ny,nx))
                    break

        ans.append([cnt,m[sy][sx]])
        return
    

    for i in range(N):
        for j in range(N):
            bfs(i,j)

    r = 0
    for i in range(len(ans)):
        r = max(r,ans[i][0])

    ck = []
    for i in range(len(ans)):
        if r == ans[i][0]:
            ck.append([ans[i][1],r])
    ck.sort()

    print(f'#{T} {ck[0][0]} {ck[0][1]}')