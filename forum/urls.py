from django.urls import path
from .views import *
from django.contrib.auth import views as authViews
from django.urls import path

urlpatterns = [
    path('', MainView.as_view(), name='home' ),
    path('user/', auto_login, name='login'),
    path('exit/', authViews.LogoutView.as_view(), name='exit'),
    path('create/', ThreadCreate.as_view(), name='create'),
    path('<str:tag>', TagView.as_view())
]
