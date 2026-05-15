from collections import deque
for tc in range(1,int(input())+1):
    n,m = map(int,input().split())
    R = [int(input()) for _ in range(n)] # 주차 공간의 단위 무게당 요금
    W = [int(input()) for _ in range(m)] # 차량 무게
    i = [int(input()) for _ in range(2*m)] # 차량 출입 순서

    parked = [0] * n # 주차 공간
    q = deque() # 주차 공간 대기열

    ans = 0

    for io in i:

        # 들어올때
        if io > 0:
            for j in range(n):
                
                # 주차 자리가 있는지
                if parked[j] == 0:
                    parked[j] = io

                    # 비용 계산
                    ans += R[j] * W[io - 1]
                    break

            # 주차 자리가 없다면 주차 대기열 추가
            else:
                q.append(io)

        # 나갈떄
        elif io < 0:
            for j in range(n):
        
                # 나가는 차량 탐색
                if parked[j] == -io:
                    parked[j] = 0
                    
                    # 주차 공간이 비기 때문에 주차 대기열에 기다리는 차가 있으면 주차 공간에 집어넣기
                    if q:
                        k = q.popleft()
                        parked[j] = k

                        # 비용 계산
                        ans += R[j] * W[k - 1]
                    break
    
    print(f'#{tc} {ans}')