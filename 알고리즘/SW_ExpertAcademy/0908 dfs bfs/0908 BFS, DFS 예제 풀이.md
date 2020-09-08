# 0908 BFS, DFS 예제 풀이

## 7465번. 창용이의 마을 무리의 개수

```python
# 7465 창용 마을 무리의 개수
def dfs(x):
    v[x] = 1
    for i in arr[x]:
        if v[i] == 0:
            v[i] = 1
            dfs(i)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    v = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if v[i] == 0:
            dfs(i)
            cnt += 1
    print(f'#{tc} {cnt}')
```

<hr>

```python
# 창용이 bfs로
def bfs(s):
    Q = [s]
    v[s] = 1
    while Q:
        w = Q.pop(0)
        v[w] = 1
        for i in arr[w]:
            if not v[i]:
                Q.append(i)
                v[i] = 1
    return 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    v = [0]*(N+1)
    cnt = 0
    for i in range(1, N+1):
        if not v[i]:
            cnt += bfs(i)
    print(f'#{tc} {cnt}')
```





## 1861. 정사각형 방

```python
# 1861. 정사각형 방


def dfs2(x, y, cnt, room_x, room_y):
    global v_max
    if cnt > v_max:
        v_max = cnt
        ans.clear()
        ans.append((cnt, arr[room_x][room_y]))
    elif cnt == v_max:
        ans.append((cnt, arr[room_x][room_y]))

    for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nx = x+i
        ny = y+j
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == arr[x][y]+1:
                dfs2(nx, ny, cnt+1, room_x, room_y)
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v_max = 1
    ans = []
    for i in range(N):
        for j in range(N):
            dfs2(i, j, 1, i, j)
    ans.sort(key=lambda x: (-x[0], x[1]))
    print(f'#{tc} {ans[0][1]} {ans[0][0]}')
```

<hr>

```python
# 정사각형방 bfs로
def check(x, y):
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x+i
        ny = y+j
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == arr[x][y]+1:
                return (nx, ny)


def bfs(x, y):
    global max_room
    global minv
    Q = [(x, y)]
    v[x][y] = 1
    cnt = 1
    while Q:
        w = Q.pop(0)
        if check(w[0], w[1]):
            x1, y1 = check(w[0], w[1])
            Q.append((x1, y1))
            v[x1][y1] = 1
            cnt += 1
    if cnt > max_room:
        max_room = cnt
        minv = arr[x][y]
    elif cnt == max_room:
        if arr[x][y] < minv:
            minv = arr[x][y]
    return (minv, cnt)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]
    max_room = 0
    minv = 99999999999999999
    ans = []
    for i in range(N):
        for j in range(N):
            if not v[i][j]:
                ans.append(bfs(i, j))
    ans.sort(key=lambda x: (-x[1], x[0]))
    print(f'#{tc} {ans[0][0]} {ans[0][1]}')
```





## 1486. 장훈이의 높은 선반

```python
# 장훈이의 높은 선반
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    x = len(lst)
    min_v = 9999999
    for i in range(1 << x):
        v = []
        for j in range(x):
            if i & (1 << j):
                v.append(lst[j])
        if (B <= sum(v)) and (sum(v) - B < min_v):
            min_v = sum(v) - B
    print(f'#{tc} {min_v}')
```

<hr>

```python
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    x = len(lst)
    min_v = 9999999
    for i in range(1 << x):
        sum_1 = 0
        for j in range(x):
            if i & (1 << j):
                sum_1 += lst[j]
        if (B <= sum_1) and (sum_1 - B < min_v):
            min_v = sum_1 - B
    print(f'#{tc} {min_v}')
```



