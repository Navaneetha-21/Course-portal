from django.urls import path
from . import views

urlpatterns=[
    path("",views.list_of_courses,name='display_courses'),
]