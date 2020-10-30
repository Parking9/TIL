def callc(x,y,sig):
    if sig== 0:
        return x+y
    elif sig == 1:
        return x-y
    elif sig ==2:
        return x*y
    else:
        return int(x/y)


def permute(n,depth,value):
    global minV
    global maxV
    if n == depth:
        if value < minV :
            minV = value
        if value > maxV:
            maxV = value
        return
    for i in range(4):
        if cal[i]>0:
            cal[i]-=1
            permute(n + 1, depth, callc(value, num[n+1], i))
            cal[i]+=1

T=int(input())
for tc in range(1, T+1):
    N=int(input())
    cal=list(map(int,input().split()))
    minV= 99999999
    maxV= -9999999
    num = list(map(int,input().split()))
    permute(0,N-1,num[0])
    print(f'#{tc} {maxV-minV}')