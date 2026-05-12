for T in range(1,int(input())+1):
    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    ans = 0

    if len(A) > len(B):
        for i in range(len(A)-len(B)+1):
            a = 0
            for j in range(len(B)):
                a += B[j] * A[i+j]
            ans = max(ans,a)

    elif len(B) > len(A):
        for i in range(len(B)-len(A)+1):
            b = 0
            for j in range(len(A)):
                b += A[j] * B[i+j]
            ans = max(ans,b)
    
    print(f'#{T} {ans}')