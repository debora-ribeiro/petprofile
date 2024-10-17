from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import serializers, status
from .serializers import PetSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

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
