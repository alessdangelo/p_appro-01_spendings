from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addUser/', views.addUser, name="addUser"),
    path('deleteUser/<int:userId>/', views.deleteUser, name="deleteUser")
]