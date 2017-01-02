from django.test import TestCase, Client
from django.urls import reverse

from .models import Category, Todo


class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.category1 = Category.objects.create(name='category1')
        self.category2 = Category.objects.create(name='category2')
        self.category3 = Category.objects.create(name='category3')

        Todo.objects.create(name='todo1', category=self.category1)
        Todo.objects.create(name='todo2', category=self.category2)
        Todo.objects.create(name='todo3', category=self.category3)

    def test_home_page_route(self):
        response = self.client.get(reverse('todos:home'))

        self.assertEqual(response.status_code, 200)

    def test_categories_exist_on_home_page(self):
        response = self.client.get(reverse('todos:home'))

        self.assertQuerysetEqual(response.context['categories'],
                                 ['<Category: category1>', '<Category: category2>',
                                  '<Category: category3>'],
                                 ordered=False)

    def test_todos_exist_on_home_page(self):
        response = self.client.get(reverse('todos:home'))

        self.assertQuerysetEqual(response.context['todos'],
                                 ['<Todo: todo1>', '<Todo: todo2>', '<Todo: todo3>'],
                                 ordered=False)


class NewTodoViewTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.category1 = Category.objects.create(name='category1')

    def test_new_todo_page_route(self):
        response = self.client.get(reverse('todos:new_todo'))

        self.assertEqual(response.status_code, 200)

    def test_new_todo_can_be_created_successfully(self):
        data = {'name': 'todo1', 'category': self.category1.id}
        response = self.client.post(reverse('todos:new_todo'), data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(Todo.objects.filter(name='todo1').exists())
        self.assertContains(response, 'todo1')
