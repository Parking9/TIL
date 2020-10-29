def removeval(lst,v):
    idx=lst.index(v)
    if idx in [0,len(lst)-1]:
        if idx == 0:
            return lst[idx+1:]
        else:
            return lst[:idx]
    else:
        return lst[:idx]+lst[idx+1:]




def goin(cn, v, cnt):
    if len(v) == 1:
        cnt += arr[cn][v[0]] + arr[v[0]][0]
        return cnt

    for i in v:
        ans.append(goin(i, removeval(v,i), cnt+arr[cn][i]))


T=int(input())
for tc in range(1,T+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    ans=[]
    goin(0,list(range(1,n)),0)
    print(f'#{tc} {min([i for i in ans if i])}')
