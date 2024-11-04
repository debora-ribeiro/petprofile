from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('cadastropets/', views.cadastrarPet, name = "cadastrarPet"),
    path('pets/', views.mostrarPets, name= "mostrarPets")
] 