for T in range(1,int(input())+1):
    N = int(input())
    num = list(sorted(map(int,input().split())))
    
    ans = {0}

    for so in num:
        for s in list(ans):
            ans.add(s+so)

    print(f'#{T} {len(ans)}')