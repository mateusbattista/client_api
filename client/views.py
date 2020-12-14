from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ClientSerializer
from .models import Cliente

# Create your views here.

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
