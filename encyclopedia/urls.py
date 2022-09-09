from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.userinput, name="userinput"),
    path("search", views.search, name="search"),
    path("newEntry", views.newEntry, name="newEntry")
]
