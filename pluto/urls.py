from django.urls import path, include
from . import views


urlpatterns = [

    path('index', views.index, name='index'),
    path('Contactdet', views.Contactdet, name='Contactdet'),
    path('deleteissue/<int:pk>/', views.deleteissue, name='deleteissue'),



]
