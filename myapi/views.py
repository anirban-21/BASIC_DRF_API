from django.shortcuts import render
from rest_framework import viewsets

from .serializers import NicknameSerializer
from .models import Nickname

# Create your views here.

class NicknameViewSet(viewsets.ModelViewSet):
    queryset = Nickname.objects.all().order_by('name')
    serializer_class = NicknameSerializer