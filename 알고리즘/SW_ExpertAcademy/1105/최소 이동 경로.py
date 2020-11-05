T=int(input())
INF = 9999999999999
for tc in range(1,T+1):
    N, E = map(int,input().split())
    arr=[[INF]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int,input().split())

        arr[s][e]=w
    for i in range(N+1):
        arr[i][i]=0

    D = arr[0]
    W = [0]*(N+1)
    cnt=0
    while cnt!=(N+1):
        cnt+=1
        maxV=INF
        for j in range(N+1):
            if W[j] == 0:
                if D[j]<maxV:
                    maxV=D[j]
                    c=j
        W[c]=1

        for k in range(N+1):
            if W[k]==0:
                if 0< arr[c][k] < INF:
                    D[k]=min(D[k],arr[c][k]+D[c])
    print(f'#{tc} {D[N]}')
