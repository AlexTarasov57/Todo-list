from django.shortcuts import render
from django.views import generic


from todo_list.models import Tag


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    template_name = "todo_list/tags_list.html"
    paginate_by = 5
