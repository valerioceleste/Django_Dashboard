from django.urls import path
from . import views

app_name = 'dash'

urlpatterns = [

    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),

]
