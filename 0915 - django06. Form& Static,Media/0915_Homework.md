# 0915_Homework

## 1번. static 파일 기본 설정

```python
# 정적 파일을 참조할 때 생성되는(사용하는) 주소
STATIC_URL = '/asset/'
# APP 내의 static 폴더 외에 추가적인 탐색 장소를 설정
STATICFILES_DIRS = [
    BASE_DIR / '프로젝트이름' / 'asset',
]
```



## 2번. media 파일 기본 설정

```python
MEDIA_URL='/uploaded_files/'
MEDIA_ROOT= BASE_DIR/'uploaded_files'
```



## 3번. Serving Files

```
(a) settings
(b) django.conf.urls.static
(c) static
(d) settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
```



