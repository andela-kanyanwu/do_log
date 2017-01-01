from django.test import TestCase, Client
from django.urls import reverse

from .models import Category


class HomeViewTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.category1 = Category.objects.create(name='category1')
        self.category2 = Category.objects.create(name='category2')
        self.category3 = Category.objects.create(name='category3')

    def test_home_page_route(self):
        response = self.client.get(reverse('todos:home'))

        self.assertEqual(response.status_code, 200)

    def test_categories_exist_on_home_page(self):
        response = self.client.get(reverse('todos:home'))

        self.assertQuerysetEqual(response.context['categories'],
                                 ['<Category: category1>', '<Category: category2>',
                                  '<Category: category3>'],
                                 ordered=False)
