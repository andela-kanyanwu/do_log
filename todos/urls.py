from django.conf.urls import url

from .views import HomeView

app_name = 'todos'
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home')
]