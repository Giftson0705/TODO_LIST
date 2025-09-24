from django.urls import path
from .views import taskList, TaskDetail


urlpatterns = [
   path('', taskList.as_view(), name='tasks'),
   path('task/<int:pk>/', TaskDetail.as_view(), name='tasks')
]