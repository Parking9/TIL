T=int(input())
for tc in range(1,T+1):
    n=float(input())
    cnt=1
    ans=''
    while (n!=0 and cnt <13):
        if n >= (2**(-1*cnt)):
            n-=(2**(-1*cnt))
            ans+='1'
        else:
            ans+='0'
        cnt+=1
    if n!=0:
        ans='overflow'
    print('#{} {}'.format(tc, ans))
