# 계산기3
def cal(a2, a1, x):
    if x == '+':
        return a2+a1
    elif x == '-':
        return a2-a1
    elif x == '*':
        return a2*a1
    else:
        return int(a2/a1)


for tc in range(1, 11):
    M = int(input())
    sent = input()
    stack = []
    v = ''
    for i in sent:
        if i == '(':
            stack.append(i)
        elif i in '*/':
            if stack[-1] in '(+-':
                stack.append(i)
            else:
                while stack[-1] not in '(+-':
                    v += stack.pop()
                stack.append(i)
        elif i in '+-':
            if stack[-1] == '(':
                stack.append(i)
            else:
                while stack[-1] != '(':
                    v += stack.pop()
                stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                v += stack.pop()
            stack = stack[:-1]
        else:
            v += i
    stack = []
    for j in v:
        if j in '-+*/':
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(cal(a2, a1, j))
        else:
            stack.append(int(j))
    print(f"#{tc} {stack.pop()}")

# Forth


def cal(x):
    if x == '+':
        return stack[-2]+stack[-1]
    elif x == '*':
        return stack[-2]*stack[-1]
    elif x == '/':
        return int(stack[-2]/stack[-1])
    else:
        return stack[-2]-stack[-1]


T = int(input())
for tc in range(1, T+1):
    v = list(input().split())
    cnt = 0
    stack = []
    for i in v:
        if i in '+-/*':
            if len(stack) < 2:
                print(f'#{tc} error')
                break
            else:
                stack = stack[:-2]+[cal(i)]
                cnt += 1
        elif i == '.':
            if cnt != len(v)-cnt-2:
                print(f'#{tc} error')
            else:
                print(f'#{tc} {stack[0]}')
        else:
            stack.append(int(i))


# 미로
# 모든 칸에 방문
def f(i, j, N):
    v[i][j] = 1
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = i+di, j+dj
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '1' and v[ni][nj] == 0:
            f(ni, nj, N)
# 조건 맞으면 종료


def f(i, j, N):
    if arr[i][j] == '3':
        return 1
    else:
        v[i][j] = 1
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != '1' and v[ni][nj] == 0:
                if f(ni, nj, N):
                    return 1
        return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    v = [[0] * N for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(N):
            if arr[i][j] == '2':
                si, sj = i, j
                break
    print(f'#{tc} {f(si,sj,N)}')

# 토너먼트 카드게임


def f(s, e):
    if s == e:
        return s
    else:
        p1 = f(s, (s+e)//2)
        p2 = f((s+e)//2+1, e)

        a = arr[p1-1]
        b = arr[p2-1]
        if [a, b] in [[1, 2], [2, 3], [3, 1]]:
            return p2
        else:
            return p1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {f(1,N)}')

# magnetic
for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


# 배열 최소합


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*N
    num = [0]*N
