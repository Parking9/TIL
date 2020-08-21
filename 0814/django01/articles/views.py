import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    menus=['치킨','피자','족발']
    pick=random.choice(menus)
    return render(request, 'dinner.html', {'pick':pick})


def hello(request,name):
    context={
        'name':name
    }
    return render(request, 'hello.html', context)


def dtl_practice(request):
    menus=['치킨','피자','족발']
    empty=[]
    context={
        'menus':menus,
        'empty':empty,
    }
    return render(request, 'dtl_practice.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # throw에서 보낸 form 데이터를 받기
    data=request.GET.get('name')
    context={
        'data':data
    }
    return render(request,'catch.html',context)