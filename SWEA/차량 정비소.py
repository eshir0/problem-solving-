from collections import deque
for T in range(1,int(input())+1):
    # N : 접수 창구, M : 정비 창구, K : 사람 수, A : n번 접수 창구를 들렸는지, B : n번 정비 창구를 들렸는지
    N, M, K, A, B = map(int,input().split())
    
    # 0번 인덱스부터 쓰기 위함.
    A -= 1
    B -= 1

    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    t = list(map(int,input().split()))

    time_A = [0] * N # 각 접수 창구가 비워지는 시간
    time_B = [0] * M # 각 정비 창구가 비워지는 시간

    # 접수 완료 기록: (끝난 시간, 이용한 접수 창구, 고객 번호)
    end = []

    # 접수 창구 통과하기
    for i in range(K):
        arr = t[i] # i번째 고객의 접수처 도착 시간

        best_j = -1 # 배정받을 창구 번호 초기화
        min_time = float('inf') # 가장 빨리 끝나는 시간을 찾기 위한 초기화

        # 바로 들어갈 수 있는 창구 찾기
        for j in range(N):
            # j번 창구가 비워지는 시간(time_A[j])이 내 도착 시간(arr)보다 작거나 같다면 빈자리 판정
            if time_A[j] <= arr:
                best_j = j
                break # 인덱스가 가장 작은 곳 우선

        # 다 꽉 찼다면 가장 빨리 끝나는 창구 찾기
        if best_j == -1:
            for j in range(N):
                # 가장 먼저 비워지는(시간이 가장 적은) 창구를 찾아서 예약
                if time_A[j] < min_time:
                    min_time = time_A[j]
                    best_j = j
        
        # 업무 처리 및 예약 장부 업데이트
        # 내가 실제 업무를 시작하는 시간: (내 도착 시간) vs (창구가 비워지는 시간) 중 늦은 시간
        start_time = max(arr, time_A[best_j])

        # 내가 끝나는 시간: 시작 시간 + j번 창구의 처리 시간
        f_time = start_time + a[best_j]

        # 다음 사람을 위해 예약 장부(time_A) 갱신: "이 창구는 f_time 이후에 쓸 수 있음"
        time_A[best_j] = f_time

        # 정비 창구로 넘기기 위한 데이터 팩킹: (끝난 시간, 이용한 창구 번호, 내 ID)
        end.append((f_time, best_j, i))

    # 일찍 접수가 끝난 순, 접수 창구 번호가 작은 순을 정리
    end.sort(key=lambda x: (x[0], x[1]))
    
    ans = 0

    for f_time, d, c_id in end:
        arr = f_time # 접수 창구에서 끝난 시간 = 정비 창구에 도착한 시간

        best_k = -1
        min_time = float('inf')

        # 바로 들어갈 수 있는 정비 창구 찾기 (접수 창구와 같음)
        for k in range(M):
            if time_B[k] <= arr:
                best_k = k
                break
        
        # 다 꽉 찼다면 가장 빨리 끝나는 정비 창구 찾기
        if best_k == -1:
            for k in range(M):
                if time_B[k] < min_time:
                    min_time = time_B[k]
                    best_k = k
        
        # 업무 처리 및 예약 장부 업데이트
        start_time = max(arr,time_B[best_k])

        # 정비 창구 예약 장부 갱신
        time_B[best_k] = start_time + b[best_k]

        # 최종 확인
        # 우리가 찾는 목표물인지 검사 -> d: 이용한 접수 창구 , best_k: 이용한 정비 창구
        # 타겟 A,B와 일치하는지 확인
        if d == A and best_k == B:
            ans += (c_id + 1) # 고객 ID는 0부터 시작했으므로 +1 해서 합산

    if ans == 0:
        ans = -1

    print(f'#{T} {ans}')