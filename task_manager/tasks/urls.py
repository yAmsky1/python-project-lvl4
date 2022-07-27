from django.urls import path
from .views import (
    TasksList,
    CreateTask,
    ChangeTask,
    DeleteTask,
    TaskView
)

app_name = 'tasks'
urlpatterns = [
    path('', TasksList.as_view(), name='list'),
    path('create/', CreateTask.as_view(), name='create'),
    path('<int:pk>/update/', ChangeTask.as_view(), name='change'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete'),
    path('<int:pk>/', TaskView.as_view(), name='viewer'),
]
