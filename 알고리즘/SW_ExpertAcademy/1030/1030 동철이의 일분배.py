def permut(n,depth,value):
    global maxV
    if value <= maxV:
        return
    if n == depth:
        if value >= maxV:
            maxV = value
        return
    else:
        for i in range(n,depth):
            lst[i], lst[n] = lst[n], lst[i]
            permut(n+1,depth, value*arr[n][lst[n]]/100)
            lst[i], lst[n] = lst[n], lst[i]


T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    lst=list(range(n))
    maxV = 0
    permut(0,n,1)
    maxV*=100
    maxV=format(maxV,'0.6f')
    print('#{} {}'.format(tc, maxV))
