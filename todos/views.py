from django.shortcuts import render
from django.views import View

from .models import Category, Todo


class HomeView(View):

    def get(self, request):
        categories = Category.objects.all()
        todos = Todo.objects.all()

        context = {
            'categories': categories,
            'todos': todos
        }

        return render(request, 'todos/home.html', context)
