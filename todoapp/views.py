from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import TodoModel
from .forms import TodoForm
from django.urls import reverse_lazy

class TodoList(ListView):
    model = TodoModel
    template_name = 'todo/list.html'
    
class TodoDetail(DetailView):
    model = TodoModel
    template_name = 'todo/detail.html'
    
class TodoCreate(CreateView):
    model = TodoModel
    form_class = TodoForm
    template_name = 'todo/create.html'
    success_url = reverse_lazy('todo_list')
    
class TodoDelete(DeleteView):
    model = TodoModel
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('todo_list')