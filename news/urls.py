
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [

    path('news/', views.news, name='news'),
    path('category', views.category, name='category'),







]
