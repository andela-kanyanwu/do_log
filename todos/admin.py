from django.contrib import admin

from .models import Category, Todo

admin.site.register([Category, Todo])
