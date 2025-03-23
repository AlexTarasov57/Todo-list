from django.urls import path

from todo_list.views import TagListView

urlpatterns = [
    path('',TagListView.as_view(),name='tag-list'),
]
