def checkrun(lst):
    for n in set(lst):
        for i in [[n-2,n-1,n],[n-1,n,n+1],[n,n+1,n+2]]:
            if list(set(lst)&set(i))==i:
                return True
    else:
        return False

def checktriple(lst):
    for i in set(lst):
        if lst.count(i)==3:
            return True
    else:
        False


T=int(input())
for tc in range(1,T+1):
    num = list(map(int, input().split()))
    p1=[num[0],num[2]]
    p2=[num[1],num[3]]
    num=num[4:]
    turn=0
    ans=0
    while num:
        cd=num.pop(0)
        if turn==0:
            p1.append(cd)
            if checkrun(p1) or checktriple(p1):
                ans= 1
                break
            else:
                turn=1
        else:
            p2.append(cd)
            if checkrun(p2) or checktriple(p2):
                ans= 2
                break
            else:
                turn=0
    if ans in [2,1]:
        print(f'#{tc} {ans}')
    else:
        print(f'#{tc} {ans}')