from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addSpending/', views.addSpending, name='addSpending'),
    path('addUser/', views.addUser, name="addUser"),
    path('deleteUser/<int:userId>/', views.deleteUser, name="deleteUser"),
    path('listSpendings/', views.listSpendings, name="listSpendings"),
    path('deleteSpending/<int:spendingId>', views.deleteSpending, name='deleteSpending'),
    path('download/', views.downloadListSpendings.as_view(), name="downloadListSpendings"),
    path('updateSpending/<int:spendingId>/', views.updateSpending, name="updateSpending")
]
