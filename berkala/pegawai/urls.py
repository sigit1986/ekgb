from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.LoginView, name='login'),
    path('logout', views.LogoutView, name='logout'),
    path('index', views.IndexView, name='index'),
    # path('welcome', views.IndexView, name='welcome'),
    #path('detail', views.IndexView, name='detail'),
    path('uploaduser', views.UploadView, name='uploaduser'),
    path('detail', views.DetailView, name = 'detail')
]
