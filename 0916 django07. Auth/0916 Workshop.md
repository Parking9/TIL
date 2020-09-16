# 0916 Workshop

## 1번. 유저목록 출력하는 페이지

```python
# views.py
from django.contrib.auth import het_user_model

def list(request):
  User=get_user_model()
  users=User.objects.all()
  context={
    'users':users
  }
  return render(request, 'accounts/list.html', context)


# urls.py의 urlpatterns에
path('', views.list, name='list'),

```

```html
{% comment %} accounts/templates/accounts/list.html {% endcomment %}

{% extends 'base.html' %}

{% block content %}
  <h1>사용자 목록</h1>
  {% for user in users %}
    <h3> {{user.username}}</h3>
  {% endfor %}
{% endblock  %}
```

<hr>

![](img/img1.gif)

## 2번. 유저 생성

```python
# urls.py의 urlpatterns안에
path('signup/',views.signup, name='signup')

# views.py
import django.contrib.auth.forms import CreateUserFrom

def signup(request):
  if request.method=='POST':
    form=UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('articles:index')
  else:
    form=UserCreationForm()
  context={
    'form':form
  }
  return render(request,'accounts/signup.html',context)
```

```html
{% comment %} accounts/templates/accounts/signup.html {% endcomment %}
{% extends 'base.html' %}

{% block content %}
  <h1 class='text-center'>회원가입</h1>
  <form action="{% url 'accounts:signup' %}" method='POST'>
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit">
  </form>
{% endblock  %}
```

![](img/img2.gif)

