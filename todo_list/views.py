from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic


from todo_list.models import Tag, Task




from django.shortcuts import redirect, get_object_or_404

from .forms import TaskForm
from .models import Task

def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.done = not task.done
    task.save()
    return redirect('todo_list:task_list')

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

    def get_queryset(self):
        sort_done = self.request.GET.get('sort', 'all')

        if sort_done == "done":
            return Task.objects.filter(done=True).order_by('-datetime_cr')
        elif sort_done == "not_done":
            return Task.objects.filter(done=False).order_by('-datetime_cr')
        return Task.objects.all().order_by('done', '-datetime_cr')


class TasksCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:task_list")


class TasksUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:task_list")


class TasksDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:task_list")