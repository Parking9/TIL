import sys
sys.stdin = open('sample_input.txt','r')


dict={
    'A':'1010',
    'B':'1011',
    'C':'1100',
    'D':'1101',
    'E':'1110',
    'F':'1111'
}

dict2={
    '0001101':'0',
    '0011001':'1',
    '0010011':'2',
    '0111101':'3',
    '0100011':'4',
    '0110001':'5',
    '0101111':'6',
    '0111011':'7',
    '0110111':'8',
    '0001011':'9'

}

def gcm1(x,y):
    n=max(x,y)
    m=min(x,y)
    while (n%m) !=0:
        m2=n%m
        n=m
        m=m2
    return m


def extract(st):
    ans=list(map(lambda x: x !='', st.strip().split('0')))
    return ans


def octotobin(st):
    ans=''
    for i in st:
        if i in dict:
            ans+=format(dict[i])
        else:
            ans+=format(int(i),'04b')
    return ans

def check(st):
    even=0
    odd=0
    for i in range(7):
        if i%2:
            even+=int(st[i])
        else:
            odd+=int(st[i])
    if (odd*3 + even + int(st[-1]))%10 == 0:
        return True
    else:
        return False


T=int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    now=[]
    for _ in range(N):
        ipt=input()
        if ipt not in now and ipt != '0'*M:
            now.append(ipt)

    lennow=len(now)
    for idx in range(len(now)):
        now[idx] = octotobin(now[idx])

    ans=[]
    for i in now:
        i=i[::-1]
        while i !='':
            cand=''
            i=i.lstrip('0')
            if i =='':
                break
            for _ in range(8):
                cnt=[0,0,0,0]
                # for j in i:
                #     if j == '1':
                #         cnt[0]+=1
                #     else:
                #         break
                # for j2 in i[cnt[0]:]:
                #     if j2 == '0':
                #         cnt[1]+=1
                #     else:
                #         break
                # for j3 in i[cnt[0]+cnt[1]:]:
                #     if j3 == '1':
                #         cnt[2]+=1
                #     else:
                #         break
                while i[0] == '1':
                    cnt[0] += 1
                    i = i[1:]
                while i[0] == '0':
                    cnt[1] += 1
                    i = i[1:]
                while i[0] == '1':
                    cnt[2] += 1
                    i = i[1:]
                gcm=gcm1(max(cnt[:-1]),min(cnt[:-1]))
                while (gcm*cnt[3] + sum(cnt[:-1])) % 7 !=0:
                    cnt[3]+=1
                cnt[3]*=gcm
                i=i[cnt[3]:]
                cnt = list(map(lambda x: x//min(cnt),cnt))

                target='0'*cnt[3]+'1'*cnt[2]+'0'*cnt[1]+'1'*cnt[0]

                cand=dict2[target]+cand
            ans.append(cand)
    ans=[ an for an in ans if check(an)==True]
    ans=list(set(ans))
    for an in range(len(ans)):
        sum1=0
        for an2 in ans[an]:
            sum1+=int(an2)
        ans[an]=sum1

    sol=sum(ans)
    print('#{} {}'.format(tc, sol))