from django.urls import path
from . import views



urlpatterns = [
    path('index/', views.index, name='index'),
    path('dinner/', views.dinner, name='dinner'),
    path('dtl-practice/', views.dtl_practice, name='dtl-practice'),
    path('throw/', views.throw, name='throw'),
    path('catch/', views.catch, name='catch'),
    path('hw/', views.hw, name='hw'),
    path('lotto/',views.lotto, name='lotto'),
    path('hello/<str:name>/', views.hello, name='hello'),#variable routing
]
