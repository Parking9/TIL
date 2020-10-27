def strchange(st,i,to):
    lenst=len(st)
    if i in [lenst, 0]:
        if i ==0:
            ans=to+st[1:]
        else:
            ans=st[:-1]+to
    else:
        ans=st[:i]+to+st[i+1:]
    return ans


def change2(n2):
    ans=[]
    len2=len(n2)
    for i in range(len2):
        n3 = n2
        if n2[i] == '0':
            ans.append(int(strchange(n3, i, '1'), 2))
        else:
            ans.append(int(strchange(n3, i, '0'), 2))
    return ans

def change3(n3):
    ans=[]
    len3=len(n3)
    for i in range(len3):
        if n3[i] == '1':
            ans.append(int(strchange(n3,i,'0'),3))
            ans.append(int(strchange(n3, i, '2'), 3))
        elif n3[i] =='2':
            ans.append(int(strchange(n3, i, '0'), 3))
            ans.append(int(strchange(n3, i, '1'), 3))
        else:
            ans.append(int(strchange(n3, i, '1'), 3))
            ans.append(int(strchange(n3, i, '2'), 3))
    return ans

T=int(input())
for tc in range(1,T+1):
    n2=input()
    n3=input()
    n2=change2(n2)
    n3=change3(n3)
    ans=list(set(n2)&set(n3))[0]

    print('#{} {}'.format(tc, ans))