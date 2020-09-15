# 0914 Workshop

## 1. Compiled Bootstrap

### project/templates/base.html

```html
{% load bootstrap4 %}

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  {% bootstrap_css %}
  {% block css %}
  {% endblock  %}
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock %}
  </div>
  {% bootstrap_javascript jquery='full' %}
</body>
</html>

```



### app/templates/app/index.html

```html
{% extends 'base.html' %}
{% load static %}

{% block css %}
  <link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
{% endblock  %}

{% block content %}

{% endblock %}

```

