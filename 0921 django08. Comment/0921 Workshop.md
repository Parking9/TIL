# 0921 Workshop

## 1. Model

```python
class Comment(models.Model):
    # 참조하는 model의 단수형으로 / 외래키가 참조하는 클래스 , on_delete (참조하는 key가 삭제되면 어떻게 할것인가)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content
```



## 2번. Comment Create, Read

```python
# forms.py에
from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields =['content',]
        # exclude=['article',]
        
        
# url.py의 patterns에

path('<int:pk>/comment/', views.comments_create,name='comments_create'),

# views.py


from .models import Comment
from .forms import CommentForm

def detail(request, pk):
    # http404 에러를 보내야하는데 500을 보내는 오류 방지를 위해
    article=get_object_or_404(Article,pk=pk)
    # article = Article.objects.get(pk=pk)
    comment_form=CommentForm()
    comments=article.comments.all()
    context = {
        'article': article,
        'comment_form' : comment_form,
        'comments':comments,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def comments_create(request, pk):
    article=get_object_or_404(Article,pk=pk)
    comment_form=CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article=article
        comment.save()
        return redirect('articles:detail', article.pk)
    context={
        'comment_form':comment_form,
        'article':article,
    }
    return render(request,'articles/detail.html', context)
```



## 4번. Delete

```python
@require_POST
def comments_create(request, pk):
    article=get_object_or_404(Article,pk=pk)
    comment_form=CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article=article
        comment.save()
        return redirect('articles:detail', article.pk)
    context={
        'comment_form':comment_form,
        'article':article,
    }
    return render(request,'articles/detail.html', context)
```



```html
{% extends 'base.html' %}

{% block content %}
  <h2 class="text-center">DETAIL</h2>
  <h3>{{ article.pk }} 번째 글</h3>
  <hr>
  <p>제목: {{ article.title }}</p>
  <p>내용: {{ article.content }}</p>
  <p>작성 시각: {{ article.created_at }}</p>
  <p>수정 시각: {{ article.updated_at }}</p>
  <hr>
  <a href="{% url 'articles:update' article.pk %}">UPDATE</a><br>
  <form action="{% url 'articles:delete' article.pk %}" method="POST">
    {% csrf_token %}
    <input type="submit" value="DELETE">
  </form>
  <a href="{% url 'articles:index' %}">[back]</a><hr>
  <h4>댓글목록</h4>
  {% if comments|length %}
    {{comments|length}}개의 댓글이 있습니다.
    {% comment %} {{comments.count}}개의 댓글이 있습니다. {% endcomment %}
  {% else %}
    <p>댓글이 없습니다.</p>
  {% endif %}

  {% for comment in comments %}
    <li>
      {{comment}}
      <form action="{% url 'articles:comments_delete' article.pk comment.pk %}" method='POST' class='d-inline'>
        {% csrf_token %}
        <input type="submit" value='댓글삭제'>
      </form>
    </li>
  {% comment %} {% empty %}
    <p>댓글이 아직 없어용..</p> {% endcomment %}
  {% endfor %}
  <hr>
  <form action="{% url 'articles:comments_create' article.pk %}" method='POST'>
    <h3>댓글 작성</h3>
    {% csrf_token %}
    {{ comment_form }}
    <input type="submit" value='작성'><hr>
  </form>
{% endblock  %}
```

