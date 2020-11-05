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
    V, E = map(int,input().split())
    arr=[]
    v=list(range(V+1))
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        arr.append([w,n1,n2])
    arr.sort(key= lambda x: x[0])

    ans=0
    for i in arr:
        if find(i[2]) != find(i[1]):
            union(i[1],i[2])
            ans+=i[0]
    print(f'#{tc} {ans}')

