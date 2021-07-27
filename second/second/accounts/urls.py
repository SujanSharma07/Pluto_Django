from django.urls import path
from .views import *
from django.views.generic import TemplateView
app_name = 'accounts'
urlpatterns = [
    path('filter/<str:status>/', home, name='home'),
    path('persons/', person_filter, name='pfilter'),
    path('create/', create_person, name='cperson'),
    path('edit/<int:id>/', edit_person, name='edit_person'),
    path('profile/<int:id>/', profile, name='profile'),
    path('delete/<int:id>/', delete, name='delete'),
    path('', signin, name='signin'),
    path('logout/', signout, name='logout'),
    path('about/', TemplateView.as_view(template_name="login.html"),name='about'),


# Class Based View
path('language/',LanguageCreate.as_view(), name='language'),
path('language/all/',LanguageList.as_view(), name='alllanguage'),
path('language/<int:pk>/',LanguageDetail.as_view(), name='ldetail'),


]

# path('filter/<str:search>')
