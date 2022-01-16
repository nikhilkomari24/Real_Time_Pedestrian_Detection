from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
import datetime
import time
from django.http import StreamingHttpResponse
from django.contrib.auth.models import User
from rest_framework.generics import (ListCreateAPIView,RetrieveUpdateDestroyAPIView,)
from rest_framework.views import APIView
from django.shortcuts import render
from django_eventstream import get_current_event_id
from django.http import HttpResponse
from django_grip import set_hold_stream
from django_eventstream import send_event

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
     return Response(data='Welcome to Home Page', status=status.HTTP_200_OK)


@api_view(['GET'])
def stream(request):
	def event_stream():
		while True:
			time.sleep(3)
			yield 'data: The server time is: %s\n\n' % datetime.datetime.now()

	a=event_stream()
	return StreamingHttpResponse(a, content_type='text/event-stream')


