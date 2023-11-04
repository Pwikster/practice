from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('task_done/<int:task_id>/', views.mark_task_done, name='mark_task_done'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
]
