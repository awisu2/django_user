from django.urls import path

from .views import login, logout

app_name = 'user'

urlpatterns = [
    # ex: /polls/
    path('', login, name='index'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
]
