from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from .models import Category, Todo
from .forms import TodoForm


class HomeView(View):

    def get(self, request):
        categories = Category.objects.all()
        todos = Todo.objects.all()

        context = {
            'categories': categories,
            'todos': todos
        }

        return render(request, 'todos/home.html', context)


class NewTodoView(View):

    def get(self, request):
        context = {
            'todo_form': TodoForm()
        }

        return render(request, 'todos/new_todo.html', context)

    def post(self, request):
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('todos:home'))

        context = {
            'form': form
        }
        return render(request, 'todos/new_todo.html', context)