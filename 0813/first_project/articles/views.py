import random
import datetime
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    menus=['족발','햄버거','치킨','초밥']
    pick=random.choice(menus)
    return render(request, 'dinner.html', {'pick' : pick})


def hello(request, name):
    context = {
        'name':name,
    }
    return render(request,'hello.html',context)


def dtl_practice(request):
    menus=['짜장면','짬뽕','볶음밥']
    empty_list=[]
    sent='하이 모두들 안녕 내가 누군지 아늬?'
    datetimenow=datetime.now()
    print(datetimenow)
    context={
        'menus':menus,
        'sentence':sent,
        'datetimenow':datetimenow,
    }
    return render(request, 'dtl_practice.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # throw에서 보낸 form 데이터를 받기
    message=request.GET.get('name')
    context={
        'message':message,
    }
    return render(request,'catch.html',context)


def hw(request):
    today=datetime.datetime.now()
    print(today)
    return render(request,'hw.html')


def lotto(request):
    numbers=list(range(1,46))
    numbers1=random.sample(numbers,5)
    numbers2=random.choice(list(set(numbers)-set(numbers1)))
    numbers1=sorted(numbers1)
    numbers1.append(numbers2)
    context={
        'ans':numbers1
    }
    return render(request,'lotto.html',context)


def trunc(request):
    sent='하이 모두들 안녕 내가 누군지 아늬?'
    context={
        'mysentence': sent
    }
    return render(request, 'dtl_practice.html',context)
