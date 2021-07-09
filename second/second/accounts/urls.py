from django.urls import path
from .views import *
urlpatterns = [
    path('filter/<str:status>/', home, name='home'),
    path('', person_filter, name='pfilter'),
    path('create/', create_person, name='cperson'),
    path('edit/<int:id>/', edit_person, name='edit_person'),
    path('profile/<int:id>/', profile, name='profile'),
    path('delete/<int:id>/', delete, name='delete'),
]

# path('filter/<str:search>')
