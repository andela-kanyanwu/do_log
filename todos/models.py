from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Todo(models.Model):

    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name