from collections import deque

def search():
    while Q:
        w=Q.popleft()
        lst = [w*2,w-10,w+1,w-1]
        for i in lst:
            if (v[i]==0) and (0< i <=1000000):
                if i != M:
                    Q.append(i)
                    v[i] = v[w] + 1
                else:
                    v[i] = v[w]
                    return

T=int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    v=[0]*1000001
    v[N]=1
    Q=deque([N])
    search()
    print(f'#{tc} {v[M]}')

# from collections import deque
# T=int(input())
# for tc in range(1,T+1):
#     N, M = map(int, input().split())
#     v={N:1}
#     Q=deque([N])
#     s=0
#     while s==0:
#         w=Q.popleft()
#         lst = [w*2,w-10,w+1,w-1]
#         for i in lst:
#             if (i not in v) and 0< i <=1000000:
#                 if i == M:
#                     s=1
#                     break
#                 Q.append(i)
#                 v[i]=v[w]+1
#     print(f'#{tc} {v[w]}')
