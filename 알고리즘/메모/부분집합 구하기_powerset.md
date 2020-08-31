# 부분집합 구하기 _ powerset

## 1번.

```python
def powerset(lst):
    result = [[]]
    for x in lst:
        newsubset = [subset + [x] for subset in result]
        result.extend(newsubset)
    return result
```



## 2번.

```python
arr=[1,2,3]
N = len(arr)
A = [0] * N

def powerset(n,k):
    if n==k:
        for i in range(n):
            if A[i]:
                print(arr[i], end=" ")
        print()
    else:
        # k번째 선택
        A[k] = 1
        powerset(n,k+1)
        # k번째 비선택
        A[k] = 0
        powerset(n,k+1)


powerset(N,0)
```

