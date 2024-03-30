from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("signUp/", views.signUp,name="signUp"),
    path("logIn/", views.logIn,name="logIn"),
    path("contact/", views.contact,name="contact"),
    path("dashboard/", views.dashboard,name="dashboard"),
    path("addBlog/", views.addBlog,name="addBlog"),
    path("edit/<int:id>/", views.edit,name="edit"),
    path("delete/<int:id>/", views.delete,name="delete"),
    path("logOut/", views.logOut,name="logOut"),
]
