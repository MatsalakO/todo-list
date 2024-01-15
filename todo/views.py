from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo.forms import TaskForm
from todo.models import Task, Tag


class IndexView(View):
    template_name = "todo/index.html"

    def get(self, request, *args, **kwargs):
        task_list = Task.objects.all().order_by("condition", "-created")
        context = {"task_list": task_list}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        if task_id:
            task = Task.objects.get(pk=task_id)
            task.condition = not task.condition
            task.save()
        return redirect("todo:index")


class TagListView(View):
    template_name = "todo/tag_list.html"

    def get(self, request, *args, **kwargs):
        tag_list = Tag.objects.all()
        context = {"tag_list": tag_list}
        return render(request, self.template_name, context)


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
