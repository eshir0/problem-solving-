for T in range(1,int(input())+1):
    li, N = input().split()
    number = list(li)
    N = int(N)

    # 같은 값 중복 제거
    v = set()
    ans = 0

    def dfs(n):
        global ans

        if n == N:
            # 바뀐 number 값 비교 -> 정답 갱신
            ans = max(ans,int(''.join(number)))
            return
        
        # 한번 이상 위치를 전환하기 때문에 - 1을 하여 하나를 남김
        for i in range(len(number) -1):
            for j in range(i+1, len(number)):
                
                # 위치 전환
                number[i],number[j] = number[j],number[i]

                # 붙여쓰기
                num = ''.join(number)
                
                # 전에 한 기록이 있는지 확인
                if (num, n+1) not in v:
                    v.add((num,n+1))
                    dfs(n+1)

                # 원상태 복귀    
                number[j],number[i] = number[i],number[j]
    
    dfs(0)
    print(f'#{T} {ans}')