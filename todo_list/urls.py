from django.urls import path

from todo_list.views import TagListView, TagsCreateView, TagsUpdateView, TagsDeleteView

urlpatterns = [
    path('tag/',TagListView.as_view(), name='tag-list'),
    path('tag/create/', TagsCreateView.as_view(), name='tag-create'),
    path('tag/<int:pk>/update/', TagsUpdateView.as_view(), name='tag-update'),
    path('tag/<int:pk>/delete/', TagsDeleteView.as_view(), name='tag-delete'),
]

app_name = 'todo_list'