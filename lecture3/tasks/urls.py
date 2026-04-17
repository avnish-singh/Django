from django.urls import path
from . import views

app_name = "tasks" # namespace for urls which is useful when we have multiple apps in our project and we want to avoid name clashes between urls of different apps
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add")
]