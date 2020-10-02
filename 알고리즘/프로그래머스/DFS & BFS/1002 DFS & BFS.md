## 3번.

```python
def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        words.insert(0,begin)
        N=len(begin)
        v=[0]*len(words)
        Q=[0]
        v[0]=1
        while Q:
            w=Q.pop(0)
            A=[x for x in words if len(set(enumerate(x))&set(enumerate(words[w])))==N-1 and v[words.index(x)]==0]
            for y in A:
                if y==target:
                    return v[w]
                Q.append(words.index(y))
                v[words.index(y)]=v[w]+1
        return 0



def solution(tickets):
    v=[0]*(len(tickets)+1)
    Q=['ICN']
    ans=['ICN']
    while Q:
        w=Q.pop(0)
        A=[x[1] for x in tickets if x[0]==w and v[tickets.index(x)]==0]
        if A!=[]:
            w2=sorted(A)[0]
            Q.append(w2)
            v[tickets.index([w,w2])]=1
            ans.append(w2)
    return ans
```



## 4번.

```python
max1=["ZZ"]*10000

def dfs(n,N,ans,v,tickets):
    global max1
    if n==N:
        an="".join(list(list(zip(*ans))[0]))
        if an < "".join(list(list(zip(*max1))[0])):
            max1= ans
        return
    for x in range(N):
        if tickets[x][0]==ans[-1] and v[x]==0:
            v[x]=1
            dfs(n+1,N,ans+[tickets[x][1]],v,tickets)
            v[x]=0


def solution(tickets):
    N=len(tickets)
    v=[0]*N
    dfs(0,N,["ICN"],v,tickets)
    return max1
```