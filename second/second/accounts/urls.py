from django.urls import path
from .views import *
urlpatterns = [
    path('filter/<str:status>/', home, name='home'),
    path('', person_filter, name='pfilter'),
    path('create/', create_person, name='cperson'),
]

# path('filter/<str:search>')
