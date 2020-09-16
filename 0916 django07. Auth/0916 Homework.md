# 0916 Homework

## 1번. Django User Model

```python
class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.
    Username and password are required. Other fields are optional.
    """
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
```



## 2번. User ModelForm

```python
from django.contrib.auth import get_user_model
```



## 3번. Decorator

```python
from django.view.decorators.http import require_POST
```

