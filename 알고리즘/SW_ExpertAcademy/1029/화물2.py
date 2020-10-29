T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    arr.sort(key=lambda x: x[1])

    f=0
    cnt=0
    for i in range(n):
        if arr[i][0] >= f:
            cnt+=1
            f=arr[i][1]
    print(f'#{tc} {cnt}')