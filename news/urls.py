
from django.urls import path
from django.urls.conf import include

from . import views

urlpatterns = [

    path('news/', views.news, name='news'),
    path('category', views.category, name='category'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('about', views.about, name='about'),
    path('donate', views.donate, name='donate'),
    # path('sattar', views.sattar, name='sattar'),









]
