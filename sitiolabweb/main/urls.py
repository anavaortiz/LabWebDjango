from django.urls import include, path
from . import views
from registro import views as v

urlpatterns = [
path("<int:id>", views.index, name="index"),
path("", views.home, name="home"),
path("home/", views.home, name="home"),
path("create/", views.create, name="create"),
path("registro/", v.register, name="registro"),
path("view/", views.view, name="vista"),
]
