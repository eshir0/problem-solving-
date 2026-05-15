# 내가 푼것
for T in range(1,int(input())+1):
    M, N = map(int,input().split())
    a = [0] + list(map(int,input().split()))
    b = [0] + list(map(int,input().split()))
    AP = [list(map(int,input().split())) for i in range(N)]

    x1,y1 = 1,1
    x2,y2 = 10,10

    ans = 0

    for i in range(M+1):
        d1 = a[i]
        d2 = b[i]
        
        if d1 == 1:
            y1 -= 1
        elif d1 == 2:
            x1 += 1
        elif d1 == 3:
            y1 += 1
        elif d1 == 4:
            x1 -= 1
        elif d1 == 0:
            pass

        if d2 == 1:
            y2 -= 1
        elif d2 == 2:
            x2 += 1
        elif d2 == 3:
            y2 += 1
        elif d2 == 4:
            x2 -= 1
        elif d2 == 0:
            pass

        A = []
        B = []
        for idx in range(N):
            x,y,c,p = AP[idx]
            if abs(x1 - x) + abs(y1 - y) <= c:
                A.append(idx)
            if abs(x2 - x) + abs(y2 - y) <= c:
                B.append(idx)
        
        if not A: A.append(-1)
        if not B: B.append(-1)

        max_p = 0
        for ca in A:
            for cb in B:
                temp_p = 0

                if ca == -1 and cb == -1:
                    temp_p = 0

                elif ca == cb and ca != -1:
                    temp_p = AP[ca][3]

                else:
                    p_A = AP[ca][3] if ca != -1 else 0
                    p_B = AP[cb][3] if cb != -1 else 0
                    temp_p = p_A + p_B

                max_p = max(max_p, temp_p)

        ans += max_p

    print(f'#{T} {ans}')

# ai가 푼것

def solve():
    # 방향: 0(이동X), 1(상), 2(우), 3(하), 4(좌)
    dx = [0, 0, 1, 0, -1]
    dy = [0, -1, 0, 1, 0]

    for T in range(1, int(input()) + 1):
        M, A_cnt = map(int, input().split())
        
        # 0초(출발)를 위해 맨 앞에 0 추가
        pathA = [0] + list(map(int, input().split()))
        pathB = [0] + list(map(int, input().split()))
        
        # AP 정보 입력 (x, y, c, p)
        APs = [list(map(int, input().split())) for _ in range(A_cnt)]

        ax, ay = 1, 1
        bx, by = 10, 10
        ans = 0

        for t in range(M + 1):
            # 1. 좌표 이동 (if-elif문 대체)
            ax += dx[pathA[t]]
            ay += dy[pathA[t]]
            bx += dx[pathB[t]]
            by += dy[pathB[t]]

            # 2. 현재 위치에서 접속 가능한 BC 후보를 한 줄로 추출 (리스트 컴프리헨션)
            candA = [i for i in range(A_cnt) if abs(ax - APs[i][0]) + abs(ay - APs[i][1]) <= APs[i][2]]
            candB = [i for i in range(A_cnt) if abs(bx - APs[i][0]) + abs(by - APs[i][1]) <= APs[i][2]]
            
            # 접속 불가 케이스(-1) 기본 추가
            candA.append(-1)
            candB.append(-1)

            # 3. 최대 충전량 탐색 (완전탐색)
            max_p = 0
            for i in candA:
                for j in candB:
                    if i == -1 and j == -1:
                        val = 0
                    elif i == j: 
                        val = APs[i][3] # 같은 BC
                    else: 
                        val = (APs[i][3] if i != -1 else 0) + (APs[j][3] if j != -1 else 0) # 다른 BC
                    
                    max_p = max(max_p, val)
            
            ans += max_p

        print(f'#{T} {ans}')

solve()