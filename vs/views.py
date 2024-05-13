from django.shortcuts import render
from rest_framework import viewsets
from .serial import DgtSerializer
from .models import DGT
from rest_framework.permissions import AllowAny
# Create your views here.

class create_view(viewsets.ModelViewSet):
    queryset = DGT.objects.all()
    serializer_class = DgtSerializer
    permission_classes = [AllowAny]