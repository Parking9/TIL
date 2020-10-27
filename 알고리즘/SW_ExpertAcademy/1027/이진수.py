T=int(input())
for tc in range(1,T+1):
    N, W = input().split()
    ans=''
    dict={
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15
    }
    for i in W:
        if i in dict:
            ans+=format(dict[i],'04b')
        else:
            ans+=format(int(i),'04b')
    print('#{} {}'.format(tc, ans))
    # print(f'#{tc} {ans}')