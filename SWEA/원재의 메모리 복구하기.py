for T in range(1,int(input())+1):
    N = list(map(int,input()))
    
    if N[0] == 1:
        ans = 1
    else:
        ans = 0
    for i in range(1,len(N)):
        if N[i-1] != N[i]:
            print(N[i-1],N[i])
            ans += 1
    
    print(ans)