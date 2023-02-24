from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addSpending/', views.addSpending, name='addSpending'),
    path('addUser/', views.addUser, name="addUser"),
    path('deleteUser/<int:userId>/', views.deleteUser, name="deleteUser"),
    path('spendings/', views.spendings, name="spendings"),
]
