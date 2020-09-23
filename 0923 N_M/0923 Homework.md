# 0923 Homework

## 1번. 1:N True or False

1) T

2)  F

3) T

4) F



## 2. ForeignKey column name

answer_id, articles_comment



## 3. 1:N ORM in template

question.comment_set.all



## 4. ?next=

Login page로 가서, 로그인을 하면 next인 delete page로 가는데 이때 redirect로 GET형식으로 간다. ( delete는 POST가 필수)

```html
http decorator( @require_POST)로 바로 막지말고 함수 안에서 막아준다.

@login_required
def delete(request, article_pk):
if request.method=='POST':
	......

```





