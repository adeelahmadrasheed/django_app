from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='index'),
    # path('articles/', views.article_serach),
 ]