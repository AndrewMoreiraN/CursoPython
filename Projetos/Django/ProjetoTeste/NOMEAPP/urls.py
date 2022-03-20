from django.urls import path
from NOMEAPP import views

urlpatterns = [
    path("", views.home, name="home"),
    path("NOMEAPP/<name>", views.hello_there, name="hello_there"),
]
