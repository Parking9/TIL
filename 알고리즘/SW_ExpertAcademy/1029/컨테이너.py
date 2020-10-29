T=int(input())
for tc in range(1,T+1):
    N, M =map(int,input().split())
    wt = list(map(int,input().split()))
    tk = list(map(int,input().split()))

    wt.sort(reverse=True)
    tk.sort(reverse=True)
    cnt=0
    while (wt != [] and tk !=[]):
        if wt[0] > tk[0]:
            wt=wt[1:]
        else:
            cnt+=wt[0]
            wt=wt[1:]
            tk=tk[1:]
    print(f'#{tc} {cnt}')