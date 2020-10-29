def maxtohead(lst):
    global n
    lenlst=len(lst)-1
    if lenlst == -1:
        return lst
    mv=max(lst)
    if lst[0]==mv:
        return [lst[0]] + maxtohead(lst[1:])
    else:
        if lst.count(mv)>1:
            a=1
            for i in range(lenlst+1):
                if lst[i] > lst[i+1]:
                    a+=1
                else:
                    break
            b=1
            for j in range(lenlst,-1,-1):
                if lst[j] == mv:
                    b+=1
                else:
                    break
            maxidx = lenlst - (lst[::-1].index(mv)+min(a,b)-1)
        else:
            maxidx = lenlst - (lst[::-1].index(mv))
        lst[0], lst[maxidx] = lst[maxidx], lst[0]
        n-=1
        return lst

def numlist_str(lst):
    ans=''
    for i in lst:
        ans+=str(i)
    return ans

def same_num_in(lst):
    for i in set(lst):
        if lst.count(i)>1:
            return True
    else:
        return False


T=int(input())
for tc in range(1,T+1):
    num, n = input().split()
    n=int(n)

    lst=[ int(i) for i in num]
    maxlst=sorted(lst,reverse=True)
    while (lst != maxlst and n !=0):
        lst=maxtohead(lst)
    n=n%2
    if n==0:
        print(f'#{tc} {numlist_str(lst)}')
    else:
        if same_num_in(lst):
            print(f'#{tc} {numlist_str(lst)}')
        else:
            lst[-2],lst[-1] = lst[-1],lst[-2]
            print(f'#{tc} {numlist_str(lst)}')
