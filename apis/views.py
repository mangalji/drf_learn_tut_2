#from django.shortcuts import render

#from rest_framework import generics

from todo.models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets

#class ListTodo(generics.ListCreateAPIView):
 #   queryset = Todo.objects.all()
  #  serializer_class = TodoSerializer

#class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
 #   queryset = Todo.objects.all()
  #  serializer_class = TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
