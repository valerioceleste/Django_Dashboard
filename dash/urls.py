from django.urls import path
from . import views

app_name = 'dash'

urlpatterns = [

    path('', views.index, name='index'),
    path('signup/', views.registration_request, name='signup'),
    path('login/', views.user_login, name='login'),

]
