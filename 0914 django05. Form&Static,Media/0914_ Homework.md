# 0914_ Homework



## 1번. 

```
(a) - fomrs.ModelForms
(b) - Meta
```



## 2번.

```
문제의 코드를 실행하면 request가 POST이며 유효성 검증을 통과하지 못한 form이 전달되지 않는다. 따라서, else 구문의 2번째 줄부터 들여쓰기를 나가 context를 받는다.
```

```python
else:
    form=ReservationForm()
context={
    'form':form
}
return render(request, 'reservation/create.html', context)
```



## 3번. 

```
(a) form=ReservationForm(request.POST, instance=reservation)
(b) form=ReservationForm(instance=reservation)
```



## 4번.

```
as_p
as_table
as_ul
```

