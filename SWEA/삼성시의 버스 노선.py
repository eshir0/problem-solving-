# P개의 버스 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램
for T in range(1,int(input())+1):
    N = int(input())

    # 5000개의 버스 정류장 배열
    stops = [0] * 5001

    # A이상 B이하의 모든 버스 정류장들 +1 (즉, 이게 답임)
    for _ in range(N):
        A,B = map(int,input().split())
        for i in range(A,B+1):
            stops[i] += 1
    
    ans = []

    # 입력갑 받는 김에 ans에다 답 갱신
    P = int(input())
    for _ in range(P):
        C = int(input())
        ans.append(stops[C])

    print(f'#{T}',*ans)