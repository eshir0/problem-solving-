# ai가 푼거
for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    m = [list(map(int, input().split())) for _ in range(N)]
    
    ans = 0
    
    # 1. 가로줄 탐색
    for i in range(N):
        cnt = 0
        for j in range(N):
            if m[i][j] == 1:
                cnt += 1 # 1을 만나면 길이 연장
            
            # 0을 만나거나, 줄의 끝(벽)에 도달했을 때 정산
            if m[i][j] == 0 or j == N - 1:
                if cnt == K: # 누적된 길이가 정확히 K와 같다면
                    ans += 1
                cnt = 0 # 정산 후 길이 초기화

    # 2. 세로줄 탐색 (i와 j의 위치만 바꿈)
    for j in range(N):
        cnt = 0
        for i in range(N):
            if m[i][j] == 1:
                cnt += 1
                
            if m[i][j] == 0 or i == N - 1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print(f'#{T} {ans}')

# 직접 푼거
for T in range(1,int(input())+1):
    N, K = map(int,input().split())
    m = [list(map(int,input().split())) for _ in range(N)]

    dy = [0,1]
    dx = [1,0]

    ans = 0

    for i in range(N):
        for j in range(N):
            if m[i][j] == 1:
                for d in range(2):
                    ny,nx = i,j
                    ny = i + dy[d]
                    nx = j + dx[d]
                    ty,tx = i,j
                    if dy[d] == 0 and dx[d] == 1:
                        tx += -1
                    elif dy[d] == 1 and dx[d] == 0:
                        ty += -1
                    if 0 > ty or 0 > tx or N <= ty or N <= tx:
                        if 0 <= ny < N and 0 <= nx < N and m[ny][nx] == 1:
                            for k in range(K-1):
                                ny += dy[d]
                                nx += dx[d]
                                if k+1 == K-1:
                                    if 0 > ny or 0 > nx or N <= ny or N <= nx:
                                        ans += 1
                                        break
                                    elif m[ny][nx] == 0:
                                        ans += 1
                                        break
                                else:
                                    if 0 > ny or 0 > nx or N <= ny or N <= nx:
                                        break
                                    elif m[ny][nx] == 0:
                                        break
                    elif 0 <= ny < N and 0 <= nx < N and m[ny][nx] == 1 and 0 <= ty < N and 0 <= tx < N and m[ty][tx] != 1:
                        for k in range(K-1):
                            ny += dy[d]
                            nx += dx[d]
                            if k+1 == K-1:
                                if 0 > ny or 0 > nx or N <= ny or N <= nx:
                                    ans += 1
                                    break
                                elif m[ny][nx] == 0:
                                    ans += 1
                                    break
                            else:
                                if 0 > ny or 0 > nx or N <= ny or N <= nx:
                                    break
                                elif m[ny][nx] == 0:
                                    break

    print(f'#{T} {ans}')