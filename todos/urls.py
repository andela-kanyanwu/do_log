from django.conf.urls import url

from .views import HomeView, NewTodoView

app_name = 'todos'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^new$', NewTodoView.as_view(), name='new_todo'),
]