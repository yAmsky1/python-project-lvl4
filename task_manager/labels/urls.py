from django.urls import path
from .views import LabelsList, CreateLabel, ChangeLabel, DeleteLabel

app_name = 'labels'
urlpatterns = [
    path('', LabelsList.as_view(), name='list'),
    path('create/', CreateLabel.as_view(), name='create'),
    path('<int:pk>/update/', ChangeLabel.as_view(), name='change'),
    path('<int:pk>/delete/', DeleteLabel.as_view(), name='delete'),
]
