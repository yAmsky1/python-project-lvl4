from django.urls import path
from .views import UsersList, CreateUser, ChangeUser, DeleteUser

app_name = 'users'
urlpatterns = [
    path('', UsersList.as_view(), name='list'),
    path('create/', CreateUser.as_view(), name='create'),
    path('<int:pk>/update/', ChangeUser.as_view(), name='change'),
    path('<int:pk>/delete/', DeleteUser.as_view(), name='delete'),
]
