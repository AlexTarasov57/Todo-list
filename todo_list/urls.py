from django.urls import path

from todo_list.views import TagListView, TagsCreateView, TagsUpdateView, TagsDeleteView, TaskListView, TasksUpdateView, \
    TasksDeleteView, TasksCreateView

urlpatterns = [
    path('tag/',TagListView.as_view(), name='tag-list'),
    path('tag/create/', TagsCreateView.as_view(), name='tag-create'),
    path('tag/<int:pk>/update/', TagsUpdateView.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagsDeleteView.as_view(), name='tag-delete'),
    path('',TaskListView.as_view(), name='task_list'),
    path('create/', TasksCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', TasksUpdateView.as_view(), name='task-update'),
    path('<int:pk>/delete/', TasksDeleteView.as_view(), name='task-delete'),
    ]

app_name = 'todo_list'