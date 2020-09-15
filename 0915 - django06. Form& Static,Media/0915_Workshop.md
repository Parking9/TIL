# 0915_Workshop

## 1번. ImageField의 Optional Argument

```python
class Article(models.Model):
    image=models.ImageField(blank=True, upload_to='%Y/%m/%d/')
```

