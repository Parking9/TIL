T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    dist=[[0]*n for _ in range(n)]

    dist[n-1][n-1]=arr[n-1][n-1]
    for i in range(n-2,-1,-1):
        dist[n-1][i] = arr[n-1][i] + dist[n-1][i+1]
        dist[i][n-1] = arr[i][n-1] + dist[i+1][n-1]

    for x in range(n-2,-1,-1):
        for y in range(n-2,-1,-1):
            dist[x][y]=arr[x][y]+min(dist[x+1][y],dist[x][y+1])
    print(f'#{tc} {dist[0][0]}')