from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, status
from .serializers import PetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pet

def index(request):
    return HttpResponse('começou')

@api_view(['POST'])
def cadastrarPet(request):
    pet_serializado = PetSerializer(data = request.data)

    if pet_serializado.is_valid():
        pet_serializado.save()
        return Response(pet_serializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def mostrarPets(request):
    lista_pets = Pet.objects.all()
    queryset_serializer = PetSerializer(lista_pets, many= True)
    return Response(queryset_serializer.data)

@api_view(['PUT'])
def atualizarPet(request, idd):
    pet = Pet.objects.get(id= idd)
    pet_serializado= PetSerializer(pet, data= request.data)
    if pet_serializado.is_valid():
        pet_serializado.save()
        return Response(pet_serializado.data, status= status.HTTP_200_OK)
    else:
        return Response(status= status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deletarPet(request, id):
    pet= Pet.objects.get(id= id)
    pet.delete()
    return Response(status= status.HTTP_204_NO_CONTENT)



