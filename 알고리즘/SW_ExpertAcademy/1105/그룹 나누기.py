def find(x):
    while v[x] != x:
        x= v[x]
    return x

def union(x,y):
    x=find(x)
    y=find(y)

    v[y]=x


T=int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    v=list(range(N+1))
    lst=list(map(int,input().split()))
    for i in range(M):
        union(lst[2*i],lst[2*i+1])
    ans=len(list(filter(lambda x: v[x]==x,list(range(N+1)))))
    ans-=1
    print(f'#{tc} {ans}')