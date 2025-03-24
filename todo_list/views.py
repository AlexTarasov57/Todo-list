from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from todo_list.models import Tag, Task


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags_list"
    template_name = "todo_list/tags_list.html"
    paginate_by = 5


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks_list"
    template_name = "todo_list/tasks_list.html"
    paginate_by = 5


class TasksCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task_list")


class TasksUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task_list")


class TasksDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task_list")