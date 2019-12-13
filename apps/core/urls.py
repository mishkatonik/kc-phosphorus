from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.get_location, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
     
]
