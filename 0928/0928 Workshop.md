# 0928 Workshop

## 1. Model

`articles/models.py`

```python
class Article(models.Model):
    like_users=models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
```



## 2. url& view

`articles/urls.py`

```python
path('<int:article_pk>/like', views.like,name='like'),
```



`articles/views.py`

```python
def like(request,article_pk):
    if request.user is_authenticated:
        article=get_object_or_404(Articles, pk=article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:index')
    return redirect('accounts:login')
```



## 3번. Template

`crud/templates/base.html`

```html
head에
<script src="https://kit.fontawesome.com/c6d30f413c.js" crossorigin="anonymous"></script>
```



`articles/templates/articles/index.html`

```html
    <form action="{% url 'articles:like' article.pk%}" method='POST' class='d-inline'>
      {% csrf_token %}
      {% if request.user in article.like_users.all %}
        <button class='btn btn-link' style='color:crimson'>
          <i class="fas fa-heart"></i>
        </button>
      {% else %}
        <button class='btn btn-link' style='color:lightgrey'>
          <i class="far fa-heart"></i>
        </button>
      {% endif %}
    </form>
```



