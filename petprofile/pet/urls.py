from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('cadastropets/', views.cadastrarPet, name = "cadastrarPet"),
    path('pets/', views.mostrarPets, name= "mostrarPets"),
    path('atualizarpet/<int:idd>', views.atualizarPet, name = "atualizarPet"),
    path('deletarpet/<int:id>', views.deletarPet, name = "deletarPet"),
    
] 