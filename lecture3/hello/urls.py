from django.urls import path
from . import views # . means current directory, so we are importing views.py from the current directory

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"), # <str:name> means that we are expecting a string parameter called name in the URL. This will be passed to the greet view as an argument.
    path("brian", views.brian, name="brian"),
    path("avnish", views.avnish, name="avnish")
]