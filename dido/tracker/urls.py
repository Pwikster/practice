from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('dido', views.main, name='main'),
    path('task_done/<int:task_id>/', views.mark_task_done, name='mark_task_done'),
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),

]
