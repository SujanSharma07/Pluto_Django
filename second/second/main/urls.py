from django.urls import path
from .views import *
app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('create/', create, name='create'),

]

# path('filter/<str:search>')
