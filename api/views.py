from django.shortcuts import render
from .models import Person
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import PersonSerializer

class PersonListView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field  = 'pk'
