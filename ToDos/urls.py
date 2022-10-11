
from django.urls import path
from . import views 
from .views import ToTaskLogin  
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.ToTaskList.as_view(), name='task-list'),
    path('totask-form', views.ToTaskCreate.as_view(), name='totask-form'),
    path('totask-update/<int:pk>/', views.ToTaskUpdate.as_view(), name='totask-update'),
    path('totask-delete/<int:pk>/' , views.ToTaskDelete.as_view(), name='totask-delete' ),
    path('totask-login', ToTaskLogin.as_view() , name='totask-login'),
    path('totask-logout', LogoutView.as_view(next_page = 'totask-login'), name='totask-logout')
]