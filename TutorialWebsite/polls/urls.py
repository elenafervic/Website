from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("index/", views.index, name="index"),#I think views.index is kind of importing the function index from views, like with numpy.array().
    #path("tableflip/", views.tableflip, name="tableflip"),
]