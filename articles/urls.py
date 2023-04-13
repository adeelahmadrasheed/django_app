from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.article_serach),
    path('article/create/', views.article_create),
    path('articles/<int:id>/', views.article_page),
]