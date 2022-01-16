from django.shortcuts import render
from rest_framework.decorators import api_view ,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

# Create your views here.

@api_view(['GET'])
def index(request):
   # date = datetime.now()
    message = 'Server is live '
    return Response(data=message, status=status.HTTP_200_OK)
