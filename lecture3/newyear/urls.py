from django.urls import path
from . import views

app_name = "newyear" # app_name is used to specify the namespace for the urls of this app. This is useful when we have multiple apps in our project and we want to avoid name clashes between urls of different apps.
urlpatterns = [
    path("", views.index, name="index"),
]