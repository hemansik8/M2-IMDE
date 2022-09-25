from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.tasks, name='tasks'),
    path('signup/', views.signup, name='signup'),
    path('details/<str:pm>/', views.taskDetails, name='details'),
    path('taskAdd/', views.taskAdd, name='add'),
    path('taskDelete/<str:id>', views.taskDelete, name='taskDelete'),
    path('taskUpdate/<str:id>', views.taskUpdate, name='taskUpdate'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

]
