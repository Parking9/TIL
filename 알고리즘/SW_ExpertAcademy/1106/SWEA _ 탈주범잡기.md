# [모의 SW 역량 테스트]

## SWEA - 탈주범 검거

```python
up=[-1,0]
right=[0,1]
down=[1,0]
left=[0,-1]

def direc(x):
    if x==up:
        return 1
    elif x==right:
        return 2
    elif x==down:
        return 3
    else:
        return 4


dict ={
    1:{1: [up, right, left],
       2: [up,down, right],
       3: [down, right, left],
       4: [up,down, left],},
    2:{1:up,3:down},
    3:{4:left, 2:right},
    4:{4:up, 3:right},
    5:{4:down, 1:right},
    6:{2:down,1:left},
    7:{2:up,3:left}
}

def


T=int(input())
for tc in range(1,T+1):
    N, M, R, C, L =map(int,input().split())
    v=[[0]*N for _ in range(N)]
    arr= [list(map(int,input().split())) for _ in range(N)]
    Q=[[0,R,C]]
    v[R][C]=1
    while Q:
        if L==0:
            break
        w=Q.pop(0)
        if w[0] != [R,C]:
            pass
        else:
            for i in list(dict[arr[w[0]][w[1]]].values())
                if 0<=w[0]+i[0]<R and 0<=w[1]+i[1]<C:
                    if v[w[0]+i[0]][w[1]+i[1]] ==0:
                        v[w[0]+i[0]][w[1]+i[1]]=v[w[0]][w[1]]+1
                        Q.append([w[0]+i[0],w[1]+i[1]])



```

