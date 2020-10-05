# 1005 Homework

## 1번

- T
- F
- **T**
- F



## 2번

- 200 : OK
- 400 : BAD_REQUEST
- 401 : UNAUTHORIZED
- 403 : FORBIDDEN
- 404 : NOT_FOUND
- 500 : INTERNAL_SERVER_ERROR



## 3번

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
```



## 4번

DB에 저장된 복잡한 형식의 Model Instance 데이터를 `JSON`이나 `XML` 따위의 형식으로 바꿔준다.