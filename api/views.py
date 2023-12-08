from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegisterSerializer

from .models import Register

@api_view(['POST'])
def create_user(request):
  serializer = RegisterSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['GET'])
def list_user(request):
  user_data = Register.objects.all()
  serializer = RegisterSerializer(user_data, many=True)
  return Response(serializer.data)
